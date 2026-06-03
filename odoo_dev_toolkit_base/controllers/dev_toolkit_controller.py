# -*- coding: utf-8 -*-

import logging

from odoo import http, _
from odoo.http import request

_logger = logging.getLogger(__name__)


class DevToolkitController(http.Controller):

    def _has_access(self):
        # Keep the launcher limited to developer users.
        return request.env.user.has_group(
            "odoo_dev_toolkit_base.group_odoo_dev_toolkit_developer"
        )

    @http.route("/odoo_dev_toolkit/tools", type="json", auth="user")
    def get_tools(self):
        if not self._has_access():
            return {"success": False, "tools": []}

        tools = request.env["odt.tool.item"].search([("active", "=", True)])
        return {
            "success": True,
            "tools": [tool.get_launcher_values() for tool in tools],
        }

    @http.route("/odoo_dev_toolkit/action", type="json", auth="user")
    def get_tool_action(self, tool_id):
        if not self._has_access():
            return {"success": False, "error": _("Access denied.")}

        try:
            tool = request.env["odt.tool.item"].browse(int(tool_id)).exists()
            if not tool or not tool.active:
                return {"success": False, "error": _("Developer tool not found.")}

            action = tool.get_action()
            if not action:
                return {
                    "success": False,
                    "error": _("The configured action could not be resolved."),
                }

            return {"success": True, "action": action}
        except Exception as error:
            _logger.exception("Unable to open developer tool.")
            return {"success": False, "error": str(error)}

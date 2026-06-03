# -*- coding: utf-8 -*-

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class OdtToolItem(models.Model):
    _name = "odt.tool.item"
    _description = "Odoo Dev Toolkit Tool"
    _order = "sequence, name"

    name = fields.Char(required=True)
    technical_name = fields.Char()
    description = fields.Text()
    category_id = fields.Many2one("odt.tool.category", string="Category")
    module_name = fields.Char()
    action_xml_id = fields.Char(required=True)
    sequence = fields.Integer(default=10)
    active = fields.Boolean(default=True)

    def get_action(self):
        """Resolve the configured action from its XML ID."""
        self.ensure_one()
        try:
            action = self.env.ref(self.action_xml_id, raise_if_not_found=False)
            if not action:
                return False
            return action.sudo().read()[0]
        except Exception:
            _logger.exception("Unable to resolve developer tool action: %s", self.action_xml_id)
            return False

    def get_launcher_values(self):
        """Tools shown in the launcher."""
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description or "",
            "category": self.category_id.name if self.category_id else "",
            "sequence": self.sequence,
            "action_xml_id": self.action_xml_id,
        }

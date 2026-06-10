# -*- coding: utf-8 -*-

from odoo import _, fields, models


class OdtViewFinderResult(models.TransientModel):
    _name = "odt.view.finder.result"
    _description = "Odoo Dev Toolkit View Finder Result"

    wizard_id = fields.Many2one(
        "odt.view.finder.wizard",
        required=True,
        ondelete="cascade",
    )
    view_id = fields.Many2one("ir.ui.view", required=True)
    view_name = fields.Char()
    model = fields.Char()
    view_type = fields.Char()
    external_id = fields.Char()
    inherit_id = fields.Many2one("ir.ui.view")
    priority = fields.Integer()
    active = fields.Boolean()
    match_count = fields.Integer()
    snippet = fields.Text()

    def action_open_view(self):
        self.ensure_one()
        # Open the technical view related to this result.
        return {
            "type": "ir.actions.act_window",
            "name": _("View"),
            "res_model": "ir.ui.view",
            "view_mode": "form",
            "res_id": self.view_id.id,
            "target": "current",
        }

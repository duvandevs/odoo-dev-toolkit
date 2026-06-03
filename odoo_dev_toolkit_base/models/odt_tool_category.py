# -*- coding: utf-8 -*-

from odoo import fields, models


class OdtToolCategory(models.Model):
    _name = "odt.tool.category"
    _description = "Odoo Dev Toolkit Tool Category"
    _order = "sequence, name"

    name = fields.Char(required=True)
    code = fields.Char(required=True)
    description = fields.Text()
    sequence = fields.Integer(default=10)
    active = fields.Boolean(default=True)

# -*- coding: utf-8 -*-
{
    "name": "Odoo Dev Toolkit - View Finder",
    "version": "17.0.1.0.0",
    "category": "Technical",
    "summary": "Search inside registered Odoo view XML records",
    "author": "duvandevs",
    "license": "LGPL-3",
    "depends": [
        "base",
        "web",
        "odoo_dev_toolkit_base",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/view_finder_views.xml",
        "data/odt_tool_item_data.xml",
    ],
    "application": False,
    "installable": True,
    "auto_install": False,
}

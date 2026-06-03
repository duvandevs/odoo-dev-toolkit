# -*- coding: utf-8 -*-
{
    "name": "Odoo Dev Toolkit - Base",
    "version": "17.0.1.0.0",
    "category": "Technical",
    "summary": "Base launcher and registry for Odoo developer tools",
    "author": "duvandevs",
    "license": "LGPL-3",
    "depends": [
        "base",
        "web",
    ],
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "data/odt_tool_category_data.xml",
        "views/odt_tool_category_views.xml",
        "views/odt_tool_item_views.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "odoo_dev_toolkit_base/static/src/js/dev_toolkit_systray.js",
            "odoo_dev_toolkit_base/static/src/xml/dev_toolkit_systray.xml",
        ],
    },
    "application": False,
    "installable": True,
    "auto_install": False,
}

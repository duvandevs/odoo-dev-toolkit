# Odoo Dev Toolkit - View Finder

View Finder is a developer tool for searching inside Odoo XML views.

It helps find fields, buttons, labels, attributes and XML snippets without manually opening each technical view. The tool is available from the `Dev Tools` launcher provided by `odoo_dev_toolkit_base`.

This module is focused on making daily Odoo view debugging faster and easier.

## How It Works

Open `Dev Tools` and select `View Finder`. Enter the text to search for, choose a search mode, optionally filter by model or view type, and run the search.

The wizard scans the `arch_db` content of registered `ir.ui.view` records and shows the matching views in a result table. Each result includes the view, model, type, external ID, inheritance information, match count and a short XML snippet around the first match.

## Search Modes

- `Contains Text`: searches the text as written.
- `Field Name`: searches XML field tags such as `<field name="partner_id"`.
- `Button Name`: searches XML button tags such as `<button name="action_confirm"`.
- `String Label`: searches XML string attributes such as `string="Customer"`.
- `Attribute`: searches XML attributes such as `invisible=`.

## Requirements

- Odoo 17.
- `base`.
- `web`.
- `odoo_dev_toolkit_base`.

## Security

Access is limited to users in the `Odoo Dev Toolkit / Developer` group from the base toolkit module.

## Current Status

This is the first stable version of View Finder. It is intended for practical developer searches in registered Odoo views and can be expanded later with richer XML parsing or advanced filters.

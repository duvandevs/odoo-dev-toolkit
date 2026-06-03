# Odoo Dev Toolkit - Base

This module provides the base structure for a modular set of developer tools for Odoo.

The goal is to keep each tool independent while sharing a common access point from the Odoo top bar. Instead of adding several menus across the backend, the module adds a simple `Dev Tools` launcher that can display any installed toolkit feature.

This base module does not include specific tools by itself. It only provides the shared registry, security group and frontend launcher used by the rest of the toolkit modules.

## Objective

`Odoo Dev Toolkit - Base` creates the common foundation for future developer-oriented modules. It gives those modules a standard way to register themselves and appear in a single top bar dropdown.

## What It Solves

Developer helpers often end up scattered across technical menus, custom side menus or temporary actions. This module keeps the main access point simple: users with the right group see `Dev Tools` in the top bar and can open any active registered tool from there.

## How It Works

The module defines two registry models:

- `odt.tool.category` groups tools by area, such as Views, Models, Imports or Security.
- `odt.tool.item` stores the tools that should appear in the launcher.

The frontend launcher requests active tools from the backend and displays them in the `Dev Tools` dropdown. When a user selects a tool, the backend resolves the configured `action_xml_id` and returns the matching Odoo action.

If no tools are registered, the dropdown shows `No developer tools available`.

## Registering Tools From Other Modules

Future toolkit modules can create records in `odt.tool.item` to appear in the launcher. The most important field is `action_xml_id`, which must point to the action that should open when the user selects the tool.

Example:

```xml
<record id="odt_tool_import_template_generator" model="odt.tool.item">
    <field name="name">Import Template Generator</field>
    <field name="technical_name">import_template_generator</field>
    <field name="description">Generate XLSX import templates from Odoo models.</field>
    <field name="category_id" ref="odoo_dev_toolkit_base.odt_tool_category_imports"/>
    <field name="module_name">odoo_import_template_generator</field>
    <field name="action_xml_id">odoo_import_template_generator.action_odoo_import_template</field>
    <field name="sequence">10</field>
</record>
```

Only active tools are shown in the launcher.

## Security

The launcher is intended for developer users only. Users must belong to the `Odoo Dev Toolkit / Developer` group to see the top bar button and request launcher data.

Developer users have read-only access to categories and registered tools. System administrators can manage the registry records from the technical views.

## Status

This module is the base layer of the toolkit. It does not include final developer tools yet. Its purpose is to provide the shared registry, security model and top bar launcher for future modules.

# Odoo Dev Toolkit

A personal Odoo developer toolkit created to simplify daily development tasks and share reusable utilities with other Odoo developers.

## Overview

This repository contains a collection of developer tools for Odoo.

The main goal is to simplify common tasks that I usually face during Odoo development, implementation and technical support. Some of these tools are created for my own workflow, but they may also be useful for other Odoo developers, technical consultants or implementers.

The project is intended to grow as a modular toolkit, where each tool can be installed only when needed instead of having one large module with every feature included.

## Purpose

Odoo development often requires repetitive technical tasks such as preparing import files, reviewing views, checking models, updating modules, debugging reports or analyzing access rules.

This toolkit is intended to group small and practical modules that help with those tasks in a cleaner and more reusable way.

The idea is not to replace Odoo's technical features, but to make some common development tasks faster and easier to access during daily work.

## Repository

GitHub repository:

```text
https://github.com/duvandevs/odoo-dev-toolkit
```

## Modules

### Odoo Dev Toolkit Base

Base module for the developer toolkit.

This module provides the common structure for future toolkit modules. It is intended to work as the shared entry point for developer tools, including a top bar launcher called `Dev Tools`.

The goal is to avoid adding too many separate backend menus and instead provide quick access to installed tools from a simple button in the Odoo top bar.

Main features:

* Adds a `Dev Tools` button in the Odoo top bar.
* Provides a shared registry for toolkit tools.
* Adds base tool categories such as Views, Models, Imports, Security, Reports and Debug.
* Adds a security group to control who can access the developer tools.
* Allows future modules to register themselves and appear in the launcher.

Status: Planned / Base structure in progress

---

### Quick Module Updater

Allows users to quickly update a specific module from anywhere in Odoo, without needing to navigate to the Apps menu and update it manually from there.

This is especially useful when working on PDF report modifications, where developers often need to apply changes and test them quickly.

Status: Done

Note: This module may remain independent from the new toolkit base for now.

---

### Odoo Import Template Generator

Generates XLSX import templates based on Odoo models and fields.

The idea is to help developers and implementers prepare import files more easily by selecting a model, choosing the fields and generating a template with useful field information.

Status: In development

---

### View XML Finder

Tool planned to search inside Odoo XML views.

The goal is to help developers quickly find fields, buttons, strings, attributes or XML snippets inside registered Odoo views without manually checking each view from the technical menu.

Possible search examples:

* Find where a field is used.
* Find a button by its technical name.
* Find labels or strings used in views.
* Search XML attributes such as `invisible`, `readonly` or `required`.
* Open the related view directly from the result.

Status: Planned

## Planned Tools

Some tools that may be added later:

* View XML Finder
* Access Rights Inspector
* Report Debug Helper
* Model Field Explorer
* External ID Finder
* Menu / Action Finder
* XPath Helper
* Record Rule Viewer
* Test Data Generator

## Target Version

* Odoo 17 Community
* Odoo 17 Enterprise

## Installation

Clone this repository and add the required module folder to your Odoo addons path.

Example:

```bash
git clone git@github.com:duvandevs/odoo-dev-toolkit.git
```

Then add the repository path or the specific module path to your Odoo configuration file.

Example:

```ini
addons_path = /path/to/odoo/addons,/path/to/odoo-dev-toolkit
```

After that, update the apps list in Odoo and install the module you want to use.

## Recommended Usage

Install only the modules you need.

For example, if you only want the base launcher and the XML view search tool in the future, you would install:

```text
odoo_dev_toolkit_base
odoo_dev_toolkit_view_xml_finder
```

If you only need the import template generator, you can install that module separately.

## Security

Some tools in this repository are intended for developers or technical users.

For that reason, toolkit modules should be restricted to the proper technical groups. The base module will include a specific security group so only allowed users can access the `Dev Tools` launcher and related tools.

## Project Status

This project is still evolving.

The first tools are focused on solving real tasks I commonly face while working with Odoo modules, reports, imports and technical debugging.

More tools will be added gradually as they become useful and stable enough to share.

## Author

Created by DuvanDevs.

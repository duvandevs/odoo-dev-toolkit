# Odoo Dev Toolkit

A personal Odoo developer toolkit created to simplify daily development tasks and share reusable utilities with other Odoo developers.

## Overview

This repository contains a modular collection of developer tools for Odoo.

The goal is to make common development, implementation and technical support tasks easier, without grouping everything into one large module. Each tool can be installed only when needed.

## Repository

```text
https://github.com/duvandevs/odoo-dev-toolkit
```

## Modules

### Odoo Dev Toolkit Base

Base module for the toolkit.

It provides the shared structure for future tools and adds a top bar launcher called `Dev Tools`, so developers can access installed tools quickly without searching through backend menus.

Main features:

* `Dev Tools` button in the Odoo top bar.
* Shared registry for toolkit tools.
* Base tool categories such as Views, Models, Imports, Security, Reports and Debug.
* Security group to control access.
* Support for future modules to register themselves in the launcher.

Status: Planned / In progress

---

### Quick Module Updater

Allows users to update a specific module quickly from anywhere in Odoo, without going manually to the Apps menu.

This is useful when working on changes that require frequent module updates, such as PDF reports or view modifications.

Status: Done

Note: This module may remain independent from the new toolkit base for now.

---

### View XML Finder

Planned tool to search inside Odoo XML views.

It will help developers find fields, buttons, strings, attributes and XML snippets inside registered Odoo views, then open the related view directly from the result.

Status: Planned

## Planned Tools

* View XML Finder
* Access Rights Inspector
* Report Debug Helper
* External ID Finder
* Menu / Action Finder
* XPath Helper

## Target Version

* Odoo 17 Community
* Odoo 17 Enterprise

## Installation

Clone the repository and add it to your Odoo addons path.

```bash
git clone git@github.com:duvandevs/odoo-dev-toolkit.git
```

Example `addons_path`:

```ini
addons_path = /path/to/odoo/addons,/path/to/odoo-dev-toolkit
```

Then update the apps list and install the module you want to use.

## Usage

Install only the tools you need.

Example:

```text
odoo_dev_toolkit_base
odoo_dev_toolkit_view_xml_finder
```

## Security

These tools are intended for developers or technical users.

The base module includes a security group so only allowed users can access the `Dev Tools` launcher and related tools.

## Status

This project is evolving gradually. The first tools are focused on real tasks I commonly face while working with Odoo modules, views, reports, imports and technical debugging.

## Author

Created by DuvanDevs.

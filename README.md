A personal Odoo developer toolkit created to simplify daily development tasks and share reusable utilities with other Odoo developers

# Odoo Dev Toolkit

This repository contains a collection of personal developer tools for Odoo.

The main goal is to simplify common tasks that I usually face during Odoo development, implementation and technical support. Some of these tools are created for my own workflow, but they may also be useful for other Odoo developers.

## Purpose

Odoo development often requires repetitive technical tasks such as preparing import files, reviewing permissions, checking models, updating modules or creating report structures.

This toolkit is intended to group small and practical modules that help with those tasks in a cleaner and more reusable way.

## Modules

### Quick Module Updater

Allows users to quickly update a specific module from anywhere in Odoo, without needing to navigate to the Apps menu and update it manually from there.

This is especially useful when working on PDF report modifications, where developers often need to apply changes and test them quickly.

Status: Done

### Odoo Import Template Generator

Generates XLSX import templates based on Odoo models and fields.

The idea is to help developers and implementers prepare import files more easily by selecting a model, choosing the fields and generating a template with useful field information.

Status: In development

## Target Version

- Odoo 17 Community
- Odoo 17 Enterprise

## Planned Tools

Some modules that may be added later:

- Quick Module Updater

## Installation

Clone this repository and add the required module folder to your Odoo addons path.

Example:

```bash
git clone git@github.com:your-user/odoo-dev-toolkit.git

# -*- coding: utf-8 -*-

from odoo import _, fields, models
from odoo.exceptions import UserError


class OdtViewFinderWizard(models.TransientModel):
    _name = "odt.view.finder.wizard"
    _description = "Odoo Dev Toolkit View Finder"

    search_text = fields.Char(required=True)
    search_mode = fields.Selection(
        [
            ("contains", "Contains Text"),
            ("field", "Field Name"),
            ("button", "Button Name"),
            ("string", "String Label"),
            ("attribute", "Attribute"),
        ],
        default="contains",
        required=True,
    )
    model_id = fields.Many2one("ir.model")
    model_name = fields.Char(related="model_id.model", store=False)
    view_type = fields.Selection(
        [
            ("form", "Form"),
            ("tree", "List"),
            ("kanban", "Kanban"),
            ("search", "Search"),
            ("qweb", "QWeb"),
            ("calendar", "Calendar"),
            ("pivot", "Pivot"),
            ("graph", "Graph"),
            ("activity", "Activity"),
        ]
    )
    active_only = fields.Boolean(default=True)
    case_sensitive = fields.Boolean(default=False)
    result_ids = fields.One2many("odt.view.finder.result", "wizard_id")

    def action_search(self):
        self.ensure_one()
        self.action_clear_results()

        if not (self.search_text or "").strip():
            raise UserError(_("Please enter a search text."))

        patterns = self._get_search_patterns()
        views = self._get_candidate_views()
        model_data_by_res_id = self._get_model_data_by_res_id(views.ids)

        result_values = []
        for view in views:
            arch = view.arch_db or ""
            match_count = self._count_matches(arch, patterns)
            if not match_count:
                continue

            result_values.append(
                {
                    "wizard_id": self.id,
                    "view_id": view.id,
                    "view_name": view.name,
                    "model": view.model,
                    "view_type": view.type,
                    "external_id": model_data_by_res_id.get(view.id, ""),
                    "inherit_id": view.inherit_id.id,
                    "priority": view.priority,
                    "active": view.active,
                    "match_count": match_count,
                    "snippet": self._get_snippet(arch, patterns),
                }
            )

        if result_values:
            self.env["odt.view.finder.result"].create(result_values)

        return self._get_wizard_action()

    def action_clear_results(self):
        self.ensure_one()
        self.result_ids.unlink()
        return self._get_wizard_action()

    def _get_candidate_views(self):
        domain = [("arch_db", "!=", False)]
        if self.model_name:
            domain.append(("model", "=", self.model_name))
        if self.view_type:
            domain.append(("type", "=", self.view_type))
        if self.active_only:
            domain.append(("active", "=", True))
        return self.env["ir.ui.view"].search(domain, order="name, id")

    def _get_search_patterns(self):
        text = (self.search_text or "").strip()
        if self.search_mode == "contains":
            return [text]
        if self.search_mode == "field":
            return self._build_named_node_patterns(text, "field")
        if self.search_mode == "button":
            return self._build_named_node_patterns(text, "button")
        if self.search_mode == "string":
            return self._build_attribute_value_patterns(text, "string")
        if self.search_mode == "attribute":
            return [text if "=" in text else "%s=" % text]
        return [text]

    def _build_named_node_patterns(self, text, node_name):
        lowered = text.lower()
        if "<%s" % node_name in lowered or "name=" in lowered:
            return [text]
        return [
            '<%s name="%s' % (node_name, text),
            "<%s name='%s" % (node_name, text),
        ]

    def _build_attribute_value_patterns(self, text, attribute_name):
        lowered = text.lower()
        if "%s=" % attribute_name in lowered:
            return [text]
        return [
            '%s="%s' % (attribute_name, text),
            "%s='%s" % (attribute_name, text),
        ]

    def _count_matches(self, arch, patterns):
        searchable_arch = arch if self.case_sensitive else arch.lower()
        total = 0
        for pattern in patterns:
            searchable_pattern = pattern if self.case_sensitive else pattern.lower()
            total += searchable_arch.count(searchable_pattern)
        return total

    def _get_snippet(self, arch, patterns):
        # Keep the original XML for the result snippet.
        position = self._find_first_match_position(arch, patterns)
        if position < 0:
            return ""

        start = max(position - 300, 0)
        end = min(position + len(patterns[0]) + 300, len(arch))
        snippet = arch[start:end].strip()
        if start:
            snippet = "...%s" % snippet
        if end < len(arch):
            snippet = "%s..." % snippet
        return snippet

    def _find_first_match_position(self, arch, patterns):
        searchable_arch = arch if self.case_sensitive else arch.lower()
        positions = []
        for pattern in patterns:
            searchable_pattern = pattern if self.case_sensitive else pattern.lower()
            position = searchable_arch.find(searchable_pattern)
            if position >= 0:
                positions.append(position)
        return min(positions) if positions else -1

    def _get_model_data_by_res_id(self, res_ids):
        if not res_ids:
            return {}

        model_data_records = self.env["ir.model.data"].sudo().search(
            [
                ("model", "=", "ir.ui.view"),
                ("res_id", "in", res_ids),
            ],
            order="module, name",
        )
        external_ids = {}
        for model_data in model_data_records:
            external_ids.setdefault(
                model_data.res_id,
                "%s.%s" % (model_data.module, model_data.name),
            )
        return external_ids

    def _get_wizard_action(self):
        return {
            "type": "ir.actions.act_window",
            "name": _("View Finder"),
            "res_model": self._name,
            "view_mode": "form",
            "res_id": self.id,
            "target": "new",
        }

/** @odoo-module **/

import { Component, onWillStart, useState } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";
import { _t } from "@web/core/l10n/translation";


export class DevToolkitSystray extends Component {
    static template = "odoo_dev_toolkit_base.DevToolkitSystray";
    static props = {};

    setup() {
        this.action = useService("action");
        this.notification = useService("notification");
        this.rpc = useService("rpc");
        this.user = useService("user");

        this.state = useState({
            canUse: false,
            isLoading: false,
            tools: [],
        });

        onWillStart(async () => {
            this.state.canUse = await this.user.hasGroup(
                "odoo_dev_toolkit_base.group_odoo_dev_toolkit_developer"
            );
        });
    }

    async onDropdownOpen() {
        if (!this.state.canUse) {
            return;
        }

        this.state.isLoading = true;
        try {
            const result = await this.rpc("/odoo_dev_toolkit/tools", {});
            this.state.tools = result.success ? result.tools || [] : [];
        } catch (error) {
            this.state.tools = [];
            this.notification.add(_t("Developer tools could not be loaded."), {
                type: "danger",
            });
        } finally {
            this.state.isLoading = false;
        }
    }

    async openTool(toolId) {
        try {
            const result = await this.rpc("/odoo_dev_toolkit/action", {
                tool_id: toolId,
            });

            if (result.success && result.action) {
                await this.action.doAction(result.action);
                return;
            }

            this.notification.add(
                result.error || _t("The selected developer tool cannot be opened."),
                { type: "warning" }
            );
        } catch (error) {
            this.notification.add(_t("The selected developer tool cannot be opened."), {
                type: "danger",
            });
        }
    }
}

registry.category("systray").add(
    "odoo_dev_toolkit_base.DevToolkitSystray",
    {
        Component: DevToolkitSystray,
    },
    { sequence: 1000 }
);

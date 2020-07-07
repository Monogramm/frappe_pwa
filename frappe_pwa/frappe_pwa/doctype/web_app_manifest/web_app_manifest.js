// Copyright (c) 2020, Monogramm and contributors
// For license information, please see license.txt

frappe.ui.form.on('Web App Manifest', {
    configure_pwa: function (frm) {
        frappe.call({
            method: 'frappe_pwa.frappe_pwa.doctype.web_app_manifest.web_app_manifest.configure_pwa',
            callback: function () {
                frappe.show_alert({message: __('Web app was configured'), indicator: 'green'})
            }
        });
    }
});

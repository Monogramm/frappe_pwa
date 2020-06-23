// Copyright (c) 2020, Monogramm and contributors
// For license information, please see license.txt

frappe.ui.form.on('Web App Manifest', {
    refresh: function (frm) {
        if (frm.doc.is_asked === 0) {
            frappe.confirm(__("Automatically configure PWA?"), function () {
                frappe.call({
                    method: 'configure_pwa',
                    doc: frm.doc,
                    callback: function () {
                        frappe.show_alert({message: __('Web app was configured'), indicator: 'green'})
                    }
                });
            }, function () {
                frm.doc.is_asked = 1;
                frm.save();
            });
        }
    }
});

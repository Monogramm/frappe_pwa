// Copyright (c) 2021, Monogramm and contributors
// For license information, please see license.txt

frappe.ui.form.on('Service Worker', {
	refresh: function(frm) {

	},
    generate_vapid_key: function (frm) {
        frappe.hide_msgprint(true);
        frappe.realtime.on("vapid_progress_bar", function (data) {
            frappe.hide_msgprint(true);
            frappe.show_progress(__("Generating VAPID key"), data.progress[0], data.progress[1]);
        });
        frappe.call({
            method: "generate_vapid_key",
            doc: cur_frm.doc,
            args: {
            },
            callback: function (r) {
				if (cur_dialog) {
					cur_dialog.hide();
				}
				if (r.message) {
					frappe.msgprint(r.message.message);
				}
                cur_frm.refresh();
            }
        });
    },
});

// Copyright (c) 2025, Bibin N and contributors
// For license information, please see license.txt


frappe.ui.form.on("Student Enrollment", {

    // Validates the form
    validate(frm) {
        let enrollmentDate = new Date(frm.doc.enrollment_date), 
            today = new Date(),
            email = frm.doc.email, 
            emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/; // Define a regex to validate email addresses

        // Check if the enrollment date is in the future
        if (enrollmentDate > today) {
            frappe.throw("Enrollment date cannot be in the future.");
        }

        // Check if the email address is valid
        if (email && !emailRegex.test(email)) {
            frappe.throw("Please enter a valid email address.");
        }
    },

    // Validate the email address input in real time.
    email: function (frm) {
        const input = frm.fields_dict.email.$input;
        const isValid = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/.test(frm.doc.email || "");

        // Add a red border if the email address is invalid
        input.css("border", isValid ? "" : "1px solid red");
    },
});


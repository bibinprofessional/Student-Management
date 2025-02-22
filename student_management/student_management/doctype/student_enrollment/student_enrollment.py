# Copyright (c) 2025, Bibin N and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.exceptions import ValidationError
from datetime import datetime
from frappe.utils import validate_email_address

class StudentEnrollment(Document):
    def validate(self):
        """Validate required fields, enrollment date, and email format."""
        
        # Validate required fields
        required_fields = ["student_name", "course", "email"]
        for fieldname in required_fields:
            if not self.get(fieldname):
                frappe.throw(f"{frappe.bold(frappe.unscrub(fieldname))} is required")

        # Validate that enrollment date is not in the future
        if self.enrollment_date:
            enrollment_date = datetime.strptime(self.enrollment_date, "%Y-%m-%d")
            if enrollment_date > datetime.today():
                frappe.throw("Enrollment date cannot be in the future.", ValidationError)

        # Validate email format
        if self.email and not validate_email_address(self.email):
            frappe.throw("Please enter a valid email address.", ValidationError)

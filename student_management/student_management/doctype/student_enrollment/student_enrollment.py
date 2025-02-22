# Copyright (c) 2025, Bibin N and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class StudentEnrollment(Document):
	def validate(self):
		"""Validate required fields"""
		required_fields = ["student_name", "course", "email"]

		for fieldname in required_fields:
			if not self.get(fieldname):
				frappe.throw(f"{frappe.bold(frappe.unscrub(fieldname))} is required")

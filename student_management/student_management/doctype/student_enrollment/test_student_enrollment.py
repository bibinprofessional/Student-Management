# Copyright (c) 2025, Bibin N and Contributors
# See license.txt

# import frappe
from frappe.tests.utils import FrappeTestCase
import frappe
from frappe.exceptions import ValidationError
from datetime import datetime, timedelta

class TestStudentEnrollment(FrappeTestCase):

	def setUp(self):
		"""Create a sample Student Enrollment document before each test."""
		self.student_enrollment = frappe.get_doc({
			"doctype": "Student Enrollment",
			"student_name": "Bibin Lal",
			"course":"Web Development",
			"email": "test@gmail.com",
			"enrollment_date": datetime.today().strftime("%Y-%m-%d"),  # Set to today
			"status": "Draft"
		})

	def test_valid_enrollment(self):
		"""Ensure a valid enrollment does not raise errors."""
		self.student_enrollment.insert()
		self.assertTrue(frappe.db.exists("Student Enrollment", self.student_enrollment.name))

	def test_future_enrollment_date(self):
		"""Ensure that an enrollment date in the future raises an error."""
		self.student_enrollment.enrollment_date = (datetime.today() + timedelta(days=1)).strftime("%Y-%m-%d")
		with self.assertRaises(ValidationError):
			self.student_enrollment.insert()

	def test_invalid_email(self):
		"""Ensure that an invalid email format raises an error."""
		self.student_enrollment.email = "bibin@gmail"
		with self.assertRaises(ValidationError):
			self.student_enrollment.insert()

	def test_valid_email(self):
		"""Ensure a valid email format does not raise errors."""
		self.student_enrollment.email = "bibin@gmail.com"
		self.student_enrollment.insert()
		self.assertTrue(frappe.db.exists("Student Enrollment", self.student_enrollment.name))

	def test_valid_transition_to_submitted(self):
		"""Ensure a valid transition from Draft → Submitted works."""
		self.student_enrollment.save()
		self.student_enrollment.status = "Submitted"
		self.student_enrollment.save()
		self.assertEqual(self.student_enrollment.status, "Submitted")

	def test_invalid_transition_direct_to_approved(self):
		"""Ensure an invalid transition from Draft → Approved is blocked."""
		self.student_enrollment.save()
		self.student_enrollment.status = "Approved"
		with self.assertRaises(ValidationError):
			self.student_enrollment.save()

	def test_valid_transition_to_approved(self):
		"""Ensure a valid transition from Submitted → Approved works."""
		self.student_enrollment.save()
  
		self.student_enrollment.status = "Submitted"
		self.student_enrollment.save()

		self.student_enrollment.status = "Approved"
		self.student_enrollment.save()

		self.assertEqual(self.student_enrollment.status, "Approved")
  
	def test_invalid_transition_direct_to_rejected(self):
		"""Ensure an invalid transition from Draft → Rejected is blocked."""
		self.student_enrollment.save()
		self.student_enrollment.status = "Rejected"
		with self.assertRaises(ValidationError):
			self.student_enrollment.save()

	def test_valid_transition_to_rejected(self):
		"""Ensure a valid transition from Submitted → Rejected works."""
		self.student_enrollment.save()
  
		self.student_enrollment.status = "Submitted"
		self.student_enrollment.save()

		self.student_enrollment.status = "Rejected"
		self.student_enrollment.save()

		self.assertEqual(self.student_enrollment.status, "Rejected")
 
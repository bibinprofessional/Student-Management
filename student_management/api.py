import frappe
from frappe.utils import validate_email_address, now, getdate

@frappe.whitelist(allow_guest=False)  # Requires authentication
def create_student_enrollment(student_name, enrollment_date, course, email):
    """Create a new Student Enrollment record with validation."""
    try:
        # Validate email format
        if not validate_email_address(email, throw=False):
            return {"status": "error", "message": "Invalid email format"}

        # Convert enrollment_date to date object if it's a string
        enrollment_date = getdate(enrollment_date)

        # Prevent future date enrollments
        if enrollment_date > getdate(now()):  
            return {"status": "error", "message": "Enrollment date cannot be in the future"}

        # Create new Student Enrollment record
        doc = frappe.get_doc({
            "doctype": "Student Enrollment",
            "student_name": student_name,
            "enrollment_date": enrollment_date,
            "course": course,
            "email": email
        })
        doc.insert()
        frappe.db.commit()

        return {"status": "success", "message": "Enrollment created successfully", "docname": doc.name}

    except Exception as e:
        frappe.log_error(f"Student Enrollment API Error: {str(e)}", "Student Enrollment API")
        return {"status": "error", "message": str(e)}


@frappe.whitelist(allow_guest=False)  # Requires authentication
def get_student_enrollments(course=None, status=None):
    """Retrieve Student Enrollment records with optional filters."""
    try:
        filters = {}
        if course:
            filters["course"] = course
        if status:
            filters["status"] = status

        enrollments = frappe.get_all(
            "Student Enrollment",
            filters=filters,
            fields=["name", "student_name", "enrollment_date", "course", "status", "email"]
        )

        return {"status": "success", "data": enrollments}

    except Exception as e:
        frappe.log_error(f"Student Enrollment Fetch Error: {str(e)}", "Student Enrollment API")
        return {"status": "error", "message": str(e)}

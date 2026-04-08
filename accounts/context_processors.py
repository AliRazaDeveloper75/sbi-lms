from .models import Student


def student_payment_status(request):
    """
    Makes payment_status, payment_expiry_date, and days_remaining
    available in every template for authenticated students.
    """
    if request.user.is_authenticated and request.user.is_student:
        try:
            student = Student.objects.get(student=request.user)
            return {
                "payment_status": student.has_active_access,
                "payment_expiry_date": student.payment_expiry_date,
                "days_remaining": student.days_remaining,
            }
        except Student.DoesNotExist:
            return {
                "payment_status": False,
                "payment_expiry_date": None,
                "days_remaining": None,
            }
    return {
        "payment_status": True,
        "payment_expiry_date": None,
        "days_remaining": None,
    }

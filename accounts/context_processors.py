from .models import Student


def student_payment_status(request):
    """
    Access rules:
    - Admin approved payment → full access always.
    - Deadline set but NOT yet passed → full access (just show a warning).
    - Deadline set AND passed AND student not paid → BLOCKED.
    - No deadline set AND student not paid → limited access (links locked).
    """
    from core.models import PaymentDeadline

    deadline = PaymentDeadline.objects.filter(is_active=True).first()

    # Non-students are never gated
    if not (request.user.is_authenticated and request.user.is_student):
        return {
            "payment_status": True,
            "payment_expiry_date": None,
            "days_remaining": None,
            "payment_deadline": deadline,
            "account_blocked": False,
            "in_grace_period": False,
        }

    try:
        student = Student.objects.get(student=request.user)
    except Student.DoesNotExist:
        return {
            "payment_status": False,
            "payment_expiry_date": None,
            "days_remaining": None,
            "payment_deadline": deadline,
            "account_blocked": False,
            "in_grace_period": False,
        }

    has_paid = student.has_active_access
    account_blocked = False
    in_grace_period = False  # True when deadline exists, not passed, student not paid

    if has_paid:
        # Paid → always full access
        effective_access = True
    elif deadline and deadline.is_active:
        if deadline.is_passed:
            # Deadline passed, not paid → BLOCKED
            effective_access = False
            account_blocked = True
        else:
            # Deadline coming but not passed → show warning, keep access
            effective_access = True
            in_grace_period = True
    else:
        # No deadline set → lock features until admin approves
        effective_access = False

    return {
        "payment_status": effective_access,
        "payment_expiry_date": student.payment_expiry_date,
        "days_remaining": student.days_remaining,
        "payment_deadline": deadline,
        "account_blocked": account_blocked,
        "in_grace_period": in_grace_period,
    }

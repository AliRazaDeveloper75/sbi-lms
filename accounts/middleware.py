from django.shortcuts import redirect
from django.urls import reverse, resolve, Resolver404


# URL names that blocked students are still allowed to visit
ALLOWED_URL_NAMES = {
    "account_blocked",
    "logout",
    "login",
    "profile",          # so they can see their payment status
    "change_password",
    "edit_profile",
}


class PaymentDeadlineMiddleware:
    """
    After the admin-set payment deadline passes, any student who hasn't
    paid is redirected to the 'account_blocked' page on every request.
    Admins, lecturers, and paid students are never affected.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and request.user.is_student:
            try:
                match = resolve(request.path_info)
                url_name = match.url_name
            except Resolver404:
                url_name = None

            if url_name not in ALLOWED_URL_NAMES:
                from django.utils import timezone
                from core.models import PaymentDeadline
                from accounts.models import Student

                deadline = PaymentDeadline.objects.filter(is_active=True).first()
                if deadline and deadline.is_passed:
                    try:
                        student = Student.objects.get(student=request.user)
                        if not student.has_active_access:
                            return redirect("account_blocked")
                    except Student.DoesNotExist:
                        return redirect("account_blocked")

        return self.get_response(request)

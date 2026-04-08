from django.contrib import admin
from .models import User, Student, Parent


class UserAdmin(admin.ModelAdmin):
    list_display = [
        "get_full_name",
        "username",
        "email",
        "is_active",
        "is_student",
        "is_lecturer",
        "is_parent",
        "is_staff",
    ]
    search_fields = [
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "is_lecturer",
        "is_parent",
        "is_staff",
    ]

    class Meta:
        managed = True
        verbose_name = "User"
        verbose_name_plural = "Users"


class StudentAdmin(admin.ModelAdmin):
    list_display = ["__str__", "level", "program", "payment_status"]
    list_editable = ["payment_status"]
    list_filter = ["payment_status", "level", "program"]
    search_fields = [
        "student__username",
        "student__first_name",
        "student__last_name",
        "student__email",
    ]
    actions = ["mark_payment_done", "mark_payment_pending"]

    def mark_payment_done(self, request, queryset):
        updated = queryset.update(payment_status=True)
        self.message_user(request, f"{updated} student(s) marked as payment done.")

    mark_payment_done.short_description = "Mark selected students as Payment Done"

    def mark_payment_pending(self, request, queryset):
        updated = queryset.update(payment_status=False)
        self.message_user(request, f"{updated} student(s) marked as payment pending.")

    mark_payment_pending.short_description = "Mark selected students as Payment Pending"


admin.site.register(User, UserAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Parent)

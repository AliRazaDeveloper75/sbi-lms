from django.contrib import admin

from .models import Session, Semester, NewsAndEvents, Notification, PaymentDeadline
from modeltranslation.admin import TranslationAdmin


class NewsAndEventsAdmin(TranslationAdmin):
    pass


class NotificationAdmin(admin.ModelAdmin):
    list_display = ["title", "is_active", "created_at"]
    list_editable = ["is_active"]
    search_fields = ["title", "message"]
    list_filter = ["is_active"]


class PaymentDeadlineAdmin(admin.ModelAdmin):
    list_display = ["deadline_date", "is_active", "is_passed", "days_until_deadline", "created_at"]
    list_editable = ["is_active"]
    readonly_fields = ["created_at"]


admin.site.register(Semester)
admin.site.register(Session)
admin.site.register(NewsAndEvents, NewsAndEventsAdmin)
admin.site.register(Notification, NotificationAdmin)
admin.site.register(PaymentDeadline, PaymentDeadlineAdmin)

from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Session, Semester, NewsAndEvents, Notification
from modeltranslation.admin import TranslationAdmin


class NewsAndEventsAdmin(TranslationAdmin):
    pass


class NotificationAdmin(admin.ModelAdmin):
    list_display = ["title", "is_active", "created_at"]
    list_editable = ["is_active"]
    search_fields = ["title", "message"]
    list_filter = ["is_active"]


admin.site.register(Semester)
admin.site.register(Session)
admin.site.register(NewsAndEvents, NewsAndEventsAdmin)
admin.site.register(Notification, NotificationAdmin)

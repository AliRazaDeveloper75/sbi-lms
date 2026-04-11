from django.db import models
from django.urls import reverse
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import AbstractUser
from django.db.models import Q
from django.utils.translation import gettext_lazy as _


NEWS = _("News")
EVENTS = _("Event")

POST = (
    (NEWS, _("News")),
    (EVENTS, _("Event")),
)

FIRST = _("First")
SECOND = _("Second")
THIRD = _("Third")

SEMESTER = (
    (FIRST, _("First")),
    (SECOND, _("Second")),
    (THIRD, _("Third")),
)


class NewsAndEventsQuerySet(models.query.QuerySet):
    def search(self, query):
        lookups = (
            Q(title__icontains=query)
            | Q(summary__icontains=query)
            | Q(posted_as__icontains=query)
        )
        return self.filter(lookups).distinct()


class NewsAndEventsManager(models.Manager):
    def get_queryset(self):
        return NewsAndEventsQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset()

    def get_by_id(self, id):
        qs = self.get_queryset().filter(
            id=id
        )  # NewsAndEvents.objects == self.get_queryset()
        if qs.count() == 1:
            return qs.first()
        return None

    def search(self, query):
        return self.get_queryset().search(query)


class NewsAndEvents(models.Model):
    title = models.CharField(max_length=200, null=True)
    summary = models.TextField(max_length=200, blank=True, null=True)
    posted_as = models.CharField(choices=POST, max_length=10)
    updated_date = models.DateTimeField(auto_now=True, auto_now_add=False, null=True)
    upload_time = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)

    objects = NewsAndEventsManager()

    def __str__(self):
        return self.title


class Session(models.Model):
    session = models.CharField(max_length=200, unique=True)
    is_current_session = models.BooleanField(default=False, blank=True, null=True)
    next_session_begins = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.session


class Semester(models.Model):
    semester = models.CharField(max_length=10, choices=SEMESTER, blank=True)
    is_current_semester = models.BooleanField(default=False, blank=True, null=True)
    session = models.ForeignKey(
        Session, on_delete=models.CASCADE, blank=True, null=True
    )
    next_semester_begins = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.semester


class ActivityLog(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"[{self.created_at}]{self.message}"


class PaymentDeadline(models.Model):
    """
    Admin sets a global payment deadline date + message.
    After this date, any student who hasn't paid is automatically blocked.
    Only one record should be active at a time.
    """
    deadline_date = models.DateField(help_text="Last date for students to complete payment.")
    message = models.TextField(
        help_text="Message shown to students about this deadline.",
        default="Please complete your payment before the deadline to avoid account suspension.",
    )
    is_active = models.BooleanField(
        default=True,
        help_text="Only one deadline should be active at a time.",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return f"Payment Deadline: {self.deadline_date}"

    @property
    def is_passed(self):
        from django.utils import timezone
        return timezone.now().date() > self.deadline_date

    @property
    def days_until_deadline(self):
        from django.utils import timezone
        delta = (self.deadline_date - timezone.now().date()).days
        return delta  # negative means already passed

    def save(self, *args, **kwargs):
        # Ensure only one active deadline at a time
        if self.is_active:
            PaymentDeadline.objects.exclude(pk=self.pk).update(is_active=False)
        super().save(*args, **kwargs)


class Notification(models.Model):
    title = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(
        default=True,
        help_text="Only active notifications are shown to students.",
    )

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.title

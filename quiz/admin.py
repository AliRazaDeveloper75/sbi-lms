from django import forms
from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TranslationAdmin
from modeltranslation.forms import TranslationModelForm

from .models import (
    Quiz,
    Progress,
    Question,
    MCQuestion,
    Choice,
    EssayQuestion,
    Sitting,
)


class ChoiceInline(admin.TabularInline):
    model = Choice


class QuizAdminForm(TranslationModelForm):
    class Meta:
        model = Quiz
        exclude = []

    questions = forms.ModelMultipleChoiceField(
        queryset=Question.objects.all(),  # Removed select_subclasses()
        required=False,
        label=_("Questions"),
        widget=FilteredSelectMultiple(verbose_name=_("Questions"), is_stacked=False),
    )

    def __init__(self, *args, **kwargs):
        super(QuizAdminForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            # Fix 1: Use 'questions' field, not 'question'
            # Fix 2: Set the initial value properly
            self.fields["questions"].initial = self.instance.question_set.all()

            # If you need to filter the available questions queryset, do it separately
            # self.fields["questions"].queryset = Question.objects.all()

    def save(self, commit=True):
        quiz = super(QuizAdminForm, self).save(commit=False)
        if commit:
            quiz.save()
        if quiz.pk:
            quiz.question_set.set(self.cleaned_data["questions"])
        else:
            quiz.save()
            quiz.question_set.set(self.cleaned_data["questions"])
        return quiz


class QuizAdmin(TranslationAdmin):
    form = QuizAdminForm
    fields = (
        "title",
        "description",
    )
    list_display = ("title",)
    search_fields = (
        "description",
        "category",
    )


class MCQuestionAdmin(TranslationAdmin):
    list_display = ("content",)
    fieldsets = [
        ("figure", {"fields": ("content", "explanation", "quiz", "choice_order")}),
    ]
    search_fields = ("content", "explanation")
    filter_horizontal = ("quiz",)
    inlines = [ChoiceInline]


class ProgressAdmin(admin.ModelAdmin):
    search_fields = (
        "user",
        "score",
    )


class EssayQuestionAdmin(admin.ModelAdmin):
    list_display = ("content",)
    fields = (
        "content",
        "quiz",
        "explanation",
    )
    search_fields = ("content", "explanation")
    filter_horizontal = ("quiz",)


admin.site.register(Quiz, QuizAdmin)
admin.site.register(MCQuestion, MCQuestionAdmin)
admin.site.register(Progress, ProgressAdmin)
admin.site.register(EssayQuestion, EssayQuestionAdmin)
admin.site.register(Sitting)

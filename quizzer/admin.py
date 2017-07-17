from django.contrib import admin

from .models import Quiz, Question, Choice, QuizSession


class ChoiceInline(admin.TabularInline):
    model = Choice
    fields = ['text', 'is_correct', 'question']


class QuestionAdmin(admin.ModelAdmin):
    fields = ['text', 'quiz']
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Quiz)
admin.site.register(QuizSession)
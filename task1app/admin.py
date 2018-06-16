from django.contrib import admin

# Register your models here.
from task1app.models import *


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_text', 'question_date')
    search_fields = ['question_text']


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'choice_text', 'choice_date', 'choice_result')
    search_fields = ['choice_text']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)

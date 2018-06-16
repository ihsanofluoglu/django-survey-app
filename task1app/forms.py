from django import forms
from task1app.models import Choice, Question


class QuestionForms(forms.ModelForm):
    class Meta:
        model = Question
        fields = {'question_title', 'question_text'}


class ChoiceForms(forms.ModelForm):
    class Meta:
        model = Choice
        fields = {'choice_text'}



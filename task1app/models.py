from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.
from django.forms import ModelForm
from django import forms


class Question(models.Model):
    question_title = models.CharField(max_length=50, default='')
    question_text = models.CharField(max_length=300)
    question_date = models.DateTimeField("Publish Data", auto_now_add=True)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question)

    choice_text = models.CharField(max_length=100, default='')
    choice_date = models.DateTimeField("Publish Data", auto_now_add=True)
    choice_result = models.IntegerField(default=0)

    def __str__(self):
        # type: () -> object
        return self.choice_text

# Create your views here.
from django.core.urlresolvers import reverse
from django.http import HttpResponse, request, HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from task1app.models import Question, Choice
from task1app.forms import QuestionForms, ChoiceForms


class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'lastest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-question_date')


class DetailView(generic.DetailView, generic.View):
    template_name = 'question_detail.html'
    model = Question

    def post(self, request, *args, **kwargs):
        if self.request.POST.get('choice'):
            ids = self.request.POST['choice']
            choice = Choice.objects.get(id=ids)
            choice.choice_result += 1
            choice.save()
            return HttpResponseRedirect('/question/%s/vote' % self.kwargs['pk'])
        else:
            return HttpResponseRedirect('/question/%s' % self.kwargs['pk'])


class QuestionView(generic.FormView):
    template_name = 'question.html'

    def get(self, request, *args, **kwargs):
        form = QuestionForms()

        return render(request, 'question.html', {'form': form})

    def post(self, request, *args, **kwargs):
        question_form = QuestionForms(self.request.POST)
        if question_form.is_valid():
            question_form.save()

        return HttpResponseRedirect('/')


class ChoiceView(generic.FormView):
    template_name = 'choice.html'
    fields = ['choice_text']

    def get(self, request, *args, **kwargs):
        form = ChoiceForms()

        return render(self.request, 'choice.html', {'form': form})

    def post(self, request, *args, **kwargs):
        choice_form = ChoiceForms(self.request.POST)
        if choice_form.is_valid():
            quest = Question.objects.get(id=self.kwargs['pk'])
            choice = choice_form.save(commit=False)
            choice.question = quest
            choice.save()

        return HttpResponseRedirect('/question/%s' % (self.kwargs['pk']))


class DeleteView(generic.DeleteView):
    model = Question
    template_name = 'delete.html'

    def get(self, request, *args, **kwargs):
        ids = self.kwargs['pk']
        quest = Question.objects.get(id=ids)
        quest.delete()

        return HttpResponseRedirect('/')


class DeleteViewChoice(generic.DeleteView):
    template_name = 'delete.html'

    def get(self, request, *args, **kwargs):
        ids = self.kwargs['id']
        choice = Choice.objects.get(id=ids)
        choice.delete()

        return HttpResponseRedirect('/question/%s' % (self.kwargs['pk']))


class VoteView(generic.DetailView):
    template_name = 'vote.html'
    model = Question


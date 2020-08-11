from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Question

import logging
LOGGER = logging.getLogger('main')

class IndexView(generic.ListView):
    template_name = 'app_base/polls/index.html'
    context_object_name = 'latest_question_list'

    context = { 'source', 'class'}
    LOGGER.debug('app_base/views::IndexView | context=' + str(context))

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'app_base/polls/detail.html'

    context = { 'source', 'class'}
    LOGGER.debug('app_base/views::DetailView | context=' + str(context))


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'app_base/polls/results.html'

    context = { 'source', 'class'}
    LOGGER.debug('app_base/views::ResultsView | context=' + str(context))


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'app_base/polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'app_base/polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'app_base/polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'app_base/polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('app_base:results', args=(question.id,)))

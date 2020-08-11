from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

import logging
LOGGER = logging.getLogger('main')

class HomeView(generic.TemplateView):
    template_name = 'app_view/home/home.html'

    context = { 'source', 'class'}
    LOGGER.debug('app_view/views::HomeView | context=' + str(context))


def index(request):
    context = { 'source', 'index'}

    LOGGER.debug('app_view/views::index | context=' + str(context))
    return render(request, 'app_view/home/index.html', context)

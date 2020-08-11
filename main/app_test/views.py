from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

import logging
LOGGER = logging.getLogger('main')

def index(request):
    context = { 'source', 'index'}

    LOGGER.debug('app_test/views::index | context=' + str(context))
    return render(request, 'app_test/home/home.html')

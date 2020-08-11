from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView 

from .models import CRUDModel 

import logging
LOGGER = logging.getLogger('main')

class CRUDHome(generic.TemplateView):
    template_name = 'app_crud/home/home.html'

    context = { 'source', 'class'}
    LOGGER.debug('app_crud/views::HomeView | context=' + str(context))

 
class CRUDCreate(CreateView): 
    template_name = 'app_crud/form/crudmodel_form.html'
    model = CRUDModel 
  
    fields = ['title', 'description']


class CRUDList(generic.ListView): 
    template_name = 'app_crud/list/index.html'
    model = CRUDModel 


def index(request):
    context = { 'source', 'index'}

    LOGGER.debug('app_crud/views::index | context=' + str(context))
    return render(request, 'app_crud/home/home.html')

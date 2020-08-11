from django.urls import path

from . import views

app_name = 'app_crud'

urlpatterns = [
    path('',     views.CRUDCreate.as_view(), name='home'),
    path('list', views.CRUDList.as_view(),   name='list'),
]

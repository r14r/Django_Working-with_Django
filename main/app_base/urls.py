from django.urls import path
from . import views

app_name = 'app_base'

urlpatterns = [
    path('', views.index, name='home'),

    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

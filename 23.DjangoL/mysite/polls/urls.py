from django.urls import path 
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('<int:question_id>/', views.detail, nmae='detail'),
	path('<int:question_id>/results/', views.resultsm, name='results'),
	path('<int:question_id>/vote/', views.vote, name='vote'),
]
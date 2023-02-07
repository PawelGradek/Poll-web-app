from django.urls import path

from . import views

app_name = 'pollapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.choice, name='choice'),
    path('<int:question_id>/score/', views.score, name='score'),
    path('<int:question_id>/user_vote/', views.user_vote, name='user_vote'),
]

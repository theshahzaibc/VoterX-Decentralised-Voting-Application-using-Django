from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_candidates/', views.get_candidates, name='get_candidates'),
    path('register_voter/', views.register_voter, name='register_voter'),
    path('start_voting/', views.start_voting, name='start_voting'),
    path('end_voting/', views.end_voting, name='end_voting'),
    path('cast_vote/', views.cast_vote, name='cast_vote'),
]

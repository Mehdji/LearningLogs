"""Defines URL patterns for learning_logs."""

from django.urls import path

from . import views

#The variable app_name helps Django distinguish this urls.py file from files 
# of the same name in other apps within the project
app_name = 'learning_logs'

urlpatterns = [
    #home page
    path('', views.index, name='index'),
    #Path that shows all topics.
    path('topics/', views.topics, name="topics"),
    path('topics/<int:topic_id>/', views.topic, name="topic"),

]
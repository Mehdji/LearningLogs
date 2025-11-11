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
    path('new_topic/', views.new_topic, name="new_topic"),
    path('new_entry/<int:topic_id>/', views.new_entry, name="new_entry"),
    path("edit_entry/<int:entry_id>/", views.edit_entry, name="edit_entry"),


]
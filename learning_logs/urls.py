"""Defines URL patterns for learning_logs."""

from django.urls import path
from . import views

app_name = 'learning_logs'

urlpatterns = [
    # Home page.
    path("", views.index, name="index"),

    # Show all topics.
    path('topics/', views.topics, name="topics"),

    # Show individual topics.
    path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
]
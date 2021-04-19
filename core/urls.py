from django.urls import path

from .views import *

urlpatterns = [
    path('feedback', get_feedback)
]

from django.urls import path

from .views import *

urlpatterns = [
    path('create_kid', create_kid),
    path('', get_parent)
]

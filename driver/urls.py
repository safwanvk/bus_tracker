from django.urls import path

from .views import *
urlpatterns = [
    path('create', create_driver),
    path('delete/<pk>', delete_driver),
    path('', get_driver)
]

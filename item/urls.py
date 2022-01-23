from django.urls import path

from .views import *

urlpatterns = [
    path('', HomePageTodo.as_view(), name='home')
]

from django.urls import path
from apps.playground.views import say_hello

urlpatterns = [
    path('playground/hello', say_hello)
]

from django.urls import path
from apps.playground.views import say_hello, say_hello_template

urlpatterns = [
    path('playground/hello', say_hello_template)
]

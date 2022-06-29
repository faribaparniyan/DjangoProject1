from django.urls import path
from myapp.views import say_hello

urlpatterns = [
    path("/hello ", say_hello)
 ]
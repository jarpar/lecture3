from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("jarek", views.jarek, name="jarek"),
    path("bob", views.bob, name="bob"),
    path("<str:name>", views.greet, name="greet")
]


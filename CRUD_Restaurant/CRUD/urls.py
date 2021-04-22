from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("restdata", views.restOP, name="restOP"),
]


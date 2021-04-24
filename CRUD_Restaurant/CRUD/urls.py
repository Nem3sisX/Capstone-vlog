from django.urls import path
from . import views

urlpatterns = [
    path("", views.index.as_view(), name="index"),
    path("restdata", views.restOP.as_view(), name="restOP"),
]


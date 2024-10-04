from django.urls import path
from django.urlspath # type: ignore

from puntuaje_app import views  # type: ignore
urlpatters = [
    path("",views.index,name="index"),
    path ("",include("puntuaje_app.urls")) # type: ignore
]
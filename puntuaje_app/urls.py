from django.urls import path
from . import views
urlpatterns =[
      path(" ",views.index,name="index"),
      path("dulce/", views.dulce,name="dulce"),
      path("minovia/",views.minovia,name="minovia"),
]
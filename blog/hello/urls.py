from django.urls import path
from . import views 

urlpatterns = [
    path("", views.index, name="index"),
    path("symo", views.symo, name="symo"),
    path("<str:name>", views.greet, name="greet")
]
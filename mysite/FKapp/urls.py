from django.urls import path
from . import views

urlpatterns = [
    path('', views.dict_lookup),
]
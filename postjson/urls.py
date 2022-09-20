from django.urls import path
from . import views

urlpatterns = [
    path('hello', views.IndexClass.as_view(), name='index'),
    path('', views.save_events_json, name='save'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexClass.as_view(), name='index'),
    path('save', views.save_events_json, name='save'),
]

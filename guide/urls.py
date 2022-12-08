from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('places/', views.place, name='place'),
    path('topics/', views.topic, name='topic'),
    path('entries/', views.entry, name='entry')
]
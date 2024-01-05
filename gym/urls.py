from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('exercise/<int:exercise_id', views.exercise_details, name='exercise_details')
]

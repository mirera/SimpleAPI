from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.urlOverview, name='endpoints'),
    path('intern/<str:pk>',views.getInternsDetails, name='interns'),
]
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.utilizatori, name='utilizatori'),
    path('om/<int:pk_id>', views.om, name='om'),
    path('results/', views.search, name='search'),
]

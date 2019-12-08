from django.urls import path

from . import views



urlpatterns = [
    path('add/', views.sighting_add, name='sighting_add'),
    path('stats/',views.sighting_stats, name='sighting_stats'),
    path('<slug:squirrel_id>/', views.sighting_update, name='sighting_update'),
    path('',views.sighting_list, name='sighting_list'),
    ]

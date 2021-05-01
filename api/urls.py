from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview, name="Flicc API Overview"), 
    path('get-speakers/', views.get_speakers, name="Get Speakers"),
    path('get-subwoofer/', views.get_subwoofer, name="Get Subwoofer"), 
    path('get-receiver/', views.get_receiver, name="Get Receiver"), 
    path('get-projector/', views.get_projector, name="Get Projector"), 
    path('get-screen/', views.get_screen, name="Get Screen"), 
]
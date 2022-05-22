from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('historia/', views.historia, name='historia'),
    path('regras/', views.regras, name='regras'),
    path('saude/', views.saude, name='saude'),
    path('sobre/', views.sobre, name='sobre')
    
    
]

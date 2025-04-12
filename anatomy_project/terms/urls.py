from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('terms/', views.terms_list, name='terms_list'),
    path('add/', views.add_term, name='add_term'),
    path('trainer/', views.trainer, name='trainer'),
    path('stats/', views.stats, name='stats'),
]

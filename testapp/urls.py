from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='test-homepage'),
    path('about/', views.about, name='test-aboutpage'),
]

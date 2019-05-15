from django.urls import path
from django.conf.urls import include

from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
]

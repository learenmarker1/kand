# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('', views.home, name='test-homepage'),
#     path('about/', views.about, name='test-aboutpage'),
# ]

from django.urls import path
from django.conf.urls import include

from . import views

app_name = 'testapp'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

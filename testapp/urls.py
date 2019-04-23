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
    path('<int:pk>/question1', views.DetailView1.as_view(), name='question1'),
    path('<int:pk>/question2', views.DetailView2.as_view(), name='question2'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:question_id>/answer1/', views.answer1, name='answer1'),
    path('<int:question_id>/answer2/', views.answer2, name='answer2'),
    path('result', views.result),
]

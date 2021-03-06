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
    path('start/', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('question1/<int:pk>/', views.DetailView1.as_view(), name='question1'),
    path('question2/<int:pk>/', views.DetailView2.as_view(), name='question2'),
    path('question3/<int:pk>/', views.DetailView3.as_view(), name='question3'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:question_id>/answer1/', views.answer1, name='answer1'),
    path('<int:question_id>/answer2/', views.answer2, name='answer2'),
    path('<int:question_id>/answer3/', views.answer3, name='answer3'),
    path('result', views.result, name='result'),
    path('teacherview', views.teacherview, name='teacherview'),
    path('', include('accounts.urls', namespace="accounts")),
    path('post/', views.post_list, name='post_list'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]

from django.urls import path

from . import views

app_name = 'library'

urlpatterns = [
    # test
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),

    # Library
    path('', views.login, name='login'),
    path('main/', views.Main.as_view(), name='main'),
    path('analysis/', views.analysis, name='analysis'),
    path('mypage/', views.mypage, name='mypage'),

]

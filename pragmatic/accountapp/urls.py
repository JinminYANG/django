from django.urls import path

from . import views

app_name = 'accountapp'
# url 처리시 편리함을 위한 사용

urlpatterns = [
    path('hello_world/', views.hello_world, name='hello_world'),
    # path('', views.index, name='index'),
    path('post_new/', views.post_new, name='post_new'),
]

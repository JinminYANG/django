from django.urls import path

from accountapp.views import hello_world

app_name = 'accountapp'
# url 처리시 편리함을 위한 사용

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world')
]
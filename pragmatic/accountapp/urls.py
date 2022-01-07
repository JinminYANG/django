from django.urls import path

from accountapp.views import hello_world

from . import views

app_name = 'accountapp'
# url 처리시 편리함을 위한 사용

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),
    # path('showmap/', showmap, name='showmap')
    # path('post_list/', views.post_list, name='post_list'),
    # path('contact/', FormView, name='contact'),
    # path('cocktail_list', cocktail_list, name='cocktail_list'),
]

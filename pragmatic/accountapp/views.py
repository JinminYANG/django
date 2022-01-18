from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views import generic, View
from django.views.decorators.csrf import csrf_exempt
from requests import Response

from accountapp.models import HelloWorld
import json

from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .forms import PostForm


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'accountapp/post_list.html', {'posts': posts})

from django.core.serializers import serialize

import requests
from django.http import JsonResponse

# In production, this should be set as an environment variable
API_KEY = 1
from django.core import serializers

def hello_world(request):
    if request.method == "POST":
        input_text = request.POST.get('hello_world_input')
        input_color = request.POST.get('team_color')

        new_hello_world = HelloWorld()
        new_hello_world.text = input_text
        new_hello_world.team_color = input_color
        new_hello_world.save()

        # hello_world_list = HelloWorld.objects.all()
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        # res = requests.get("https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita")
        # res_serialized = json.loads(serializers.serialize('json', res))

        context = {
            'hello_world_list' : HelloWorld.objects.all(),
            'post_lists' : Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date'),
            # 'json_res' : JsonResponse(res_serialized, safe=False),
            # 'res': res,
        }

        return HttpResponseRedirect(reverse('accountapp:hello_world'))
    else:
        # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

        # res = requests.get("https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita")
        # res_serialized = json.dumps(serializers.serialize('json', res))

        context = {
            'hello_world_list': HelloWorld.objects.all(),
            'posts':  Post.objects.all(),
            # 'res': json.loads(serializers.serialize('json', res)),
            # 'res': res,
        }

        return render(request, 'accountapp/hello_world.html', context=context)

'''
@csrf_exempt
def showmap(request, tbl_person_info_id, TBL_PERSON_INFO=None):
    person = TBL_PERSON_INFO.objects.get(id=tbl_person_info_id)
    persondict = {
        'lat': person.deviceid.latitude,
        'lon': person.deviceid.longitude,
        'station': person.deviceid.station
    }
    personJson = json.dumps(persondict)
    return render(request, 'map.html', {'personJson': personJson})
'''

'''
from .apicodes import keyword

class FormView(generic.View): #formtest
    template_name = 'acctountapp/contact.html'

    def post(self,request):
        inputkw = request.POST.get('name')
        result = keyword.keywordFindAPI(inputkw)
        context ={
            'result' : result
        }
        return render(request,self.template_name,context)
'''

from .forms import NameForm

def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)

        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/myform/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'myform/name.html', {'form': form})

def thanks(request):
    return render(request, 'myform/thanks.html')

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES) # NOTE: 인자 순서주의 POST, FILES
        if form.is_valid():
            post = form.save()
            return redirect(post)
    else:
        form = PostForm()
        return render(request, 'post_form.html', {'form': form})	# 검증에 실패시 form.error 에 오류 정보를 저장하여 함께 렌더링


import json

def test(request):
    list = [1, 2, 3, 4, 5]
    json_list = json.dumps(list)
    context = json_list
    return render(request, 'accountapp/test.html', context)
    # render_to_response() 는 Django에서 deprecated 되었음


class TestView(View):
    def post(self, request):
        user_id = request.POST.get('user_id')
        return Response()


def main(request):
    return render(request, 'main.html')


def corporate_statistics(request):
    return render(request, 'corporate_statistics.html')


def mypage(request):
    return render(request, 'mypage.html')


def login(request):
    return render(request, 'login.html')
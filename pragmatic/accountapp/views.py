from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.template import context
from django.urls import reverse
from django.views import generic, View
from django.views.decorators.csrf import csrf_exempt
# from requests import Response
from requests import request

import json

from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .forms import PostForm


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'accountapp/post_list.html', {'posts': posts})


from django.core.serializers import serialize

# import requests
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
            'hello_world_list': HelloWorld.objects.all(),
            'post_lists': Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date'),
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
            'posts': Post.objects.all(),
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
        form = PostForm(request.POST, request.FILES)  # NOTE: ?????? ???????????? POST, FILES
        if form.is_valid():
            post = form.save()
            return redirect(post)
    else:
        form = PostForm()
        return render(request, 'post_form.html', {'form': form})  # ????????? ????????? form.error ??? ?????? ????????? ???????????? ?????? ?????????


import json


def test(request):
    list = [1, 2, 3, 4, 5]
    json_list = json.dumps(list)
    context = json_list
    return render(request, 'accountapp/test.html', context)
    # render_to_response() ??? Django?????? deprecated ?????????


class TestView(View):
    def post(self, request):
        user_id = request.POST.get('user_id')
        return Response()


class mainView(LoginRequiredMixin):
    template_name = 'comLib/main.html'
    login_url = '/login/'

    ordering = ['-pk']
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


# MILcomLib
# data context text ?????????
'''
def main(request):
    context = datetime

    return render(request, 'main.html', {
        'date': '2021??? 11???',
        'company_read_data': {
            'count': 5,
            'hours': 1,
            'minute': 45,
        },
        'user_rank': {
            'list': [
                ['aixcon1', 5],
                ['aixcon2', 4],
                ['aixcon3', 3],
                ['aixcon4', 2],
                ['aixcon5', 1],
            ]
        },
        'user_rank2': {
            'test01': {
                'title': 'aixcon01',
                'count': 5,
            },
            'test02': {
                'title': 'aixcon02',
                'count': 4,
            },
            'test03': {
                'title': 'aixcon03',
                'count': 3,
            },
            'test04': {
                'title': 'aixcon04',
                'count': 2,
            },
            'test05': {
                'title': 'aixcon05',
                'count': 1,
            },
        },
        'user_rank3': {
            {
                'title': 'aixcon01',
                'count': 5,
            },
            {
                'title': 'aixcon02',
                'count': 4,
            },
            {
                'title': 'aixcon03',
                'count': 3,
            },
            {
                'title': 'aixcon04',
                'count': 2,
            },
            {
                'title': 'aixcon05',
                'count': 1,
            },
        },
        'book_rank': {
            'title': '???????????? ??? ??????????????? ??????',
            'author': '???????????? ????????????',
            'count': 15,
        },
        'category': {
            'title': '??????',
            'percentage': 35,
        },
        'my_reading_record': {
            'time': 20,
            'best_category': '??????',
            'best_count': 7,
            'list': [
                ['??????', 7],
                ['??????', 5],
                ['?????????', 2],
            ],
        },
        'board': {
            'list': [
                ['2022??? 1??????', '2021-12-30'],
                ['2021??? 12??????', '2021-11-28'],
                ['2021??? 11??????', '2021-10-31'],
                ['2021??? 10??????', '2021-09-30'],
                ['2021??? 9??????', '2021-08-31'],
            ],
        },
        'notice': {
            'list': [
                ['?????????', '2021 ?????? ????????? ?????? ?????? ??????', '2021-12-30'],
                ['??????', '1?????? ??? ????????? ??? ????????? ??????????????????', '2021-11-28'],
                ['??????', '????????? ?????? ?????? ?????? ????????? ????????????', '2021-10-31'],
                ['?????????', '????????? ?????? ??????, ????????? ??????', '2021-09-30'],
                ['??????', '11??? ????????? ?????? ?????? ??????', '2021-08-31'],
            ],
        },
    })
'''

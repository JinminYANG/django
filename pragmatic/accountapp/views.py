from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views import generic, View
from django.views.decorators.csrf import csrf_exempt
# from requests import Response

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
        form = PostForm(request.POST, request.FILES)  # NOTE: 인자 순서주의 POST, FILES
        if form.is_valid():
            post = form.save()
            return redirect(post)
    else:
        form = PostForm()
        return render(request, 'post_form.html', {'form': form})  # 검증에 실패시 form.error 에 오류 정보를 저장하여 함께 렌더링


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


class mainView(LoginRequiredMixin):
    template_name = 'comLib/main.html'
    login_url = '/login/'

    ordering = ['-pk']
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


# MILcomLib
# data context text 진행중
def main(request):
    return render(request, 'main.html', {
        'date': '2021년 11월',
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
        '''
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
        '''
        'book_rank': {
            'title': '주말에는 더 행복하기로 했다',
            'author': '카트리나 온스태드',
            'count': 15,
        },
        'category': {
            'title': '소설',
            'percentage': 35,
        },
        'my_reading_record': {
            'time': 20,
            'best_category': '소설',
            'best_count': 7,
            'list': [
                ['소설', 7],
                ['만화', 5],
                ['에세이', 2],
            ],
        },
        'board': {
            'list': [
                ['2022년 1월호', '2021-12-30'],
                ['2021년 12월호', '2021-11-28'],
                ['2021년 11월호', '2021-10-31'],
                ['2021년 10월호', '2021-09-30'],
                ['2021년 9월호', '2021-08-31'],
            ],
        },
        'notice': {
            'list': [
                ['이벤트', '2021 연말 다독왕 시상 결과 발표', '2021-12-30'],
                ['공지', '1월에 꼭 읽어야 할 도서를 추천해주세요', '2021-11-28'],
                ['공지', '밀리의 서재 기업 회원 구독권 이용하기', '2021-10-31'],
                ['이벤트', '겨울은 연말 독서, 다독왕 선정', '2021-09-30'],
                ['공지', '11월 회장님 추천 도서 목록', '2021-08-31'],
            ],
        },
    })


def analysis(request):
    return render(request, 'analysis.html')


def mypage(request):
    return render(request, 'mypage.html')


def login(request):
    return render(request, 'login.html')

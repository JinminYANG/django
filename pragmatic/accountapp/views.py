from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views import generic
from django.views.decorators.csrf import csrf_exempt

from accountapp.models import HelloWorld
import json

from django.shortcuts import render
from django.utils import timezone
from .models import Post


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

        hello_world_list = HelloWorld.objects.all()
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        res = requests.get("https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita")
        # res_serialized = json.loads(serializers.serialize('json', res))

        context = {
            'hello_world_list' : HelloWorld.objects.all(),
            'post_lists' : Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date'),
            # 'json_res' : JsonResponse(res_serialized, safe=False),
            'res': res,
        }

        return HttpResponseRedirect(reverse('accountapp:hello_world'))
    else:
        res = requests.get("https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita")
        # res_serialized = json.dumps(serializers.serialize('json', res))

        context = {
            'hello_world_list': HelloWorld.objects.all(),
            'posts': Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date'),
            # 'res': json.loads(serializers.serialize('json', res)),
            'res': res,
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

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views import generic
from django.views.decorators.csrf import csrf_exempt

from accountapp.models import HelloWorld
import json

def hello_world(request):
    if request.method == "POST":
        input_text = request.POST.get('hello_world_input')
        input_color = request.POST.get('team_color')

        new_hello_world = HelloWorld()
        new_hello_world.text = input_text
        new_hello_world.team_color = input_color
        new_hello_world.save()

        hello_world_list = HelloWorld.objects.all()
        return HttpResponseRedirect(reverse('accountapp:hello_world'))
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})

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
    template_name = 'apitest/contact.html'

    def post(self,request):
        inputkw = request.POST.get('name')
        result = keyword.keywordFindAPI(inputkw)
        context ={
            'result' : result
        }
        return render(request,self.template_name,context)
'''


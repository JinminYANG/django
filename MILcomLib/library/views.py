from django.contrib.auth.models import User
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView

from .models import Question, Statistics, Company, StatisticsMember, StatisticsBestBook, StatisticsBestCategory
from django.shortcuts import render

# test
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)



# Library
class Main(TemplateView):
    template_name = 'main.html'

    def get_queryset(self):
        self.user = get_object_or_404(User, username=self.kwargs['company_name'])
        self.company = get_object_or_404(Company, user=self.user)
        self.statistics = Statistics.objects.filter(company=self.company).order_by('-statistics_month')
        return self.statistics

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company'] = self.company
        context['latest_question_list'] = Question.objects.order_by('-pub_date')[:5]
        # context['date'] = Question.pub_date
        # context['company'] = Company.objects.all()
        context['company_read_data'] = {'count': 5, 'hours': 1, 'minute': 45}
        context['statistics'] = Statistics.objects.all()

        return context



def analysis(request):
    return render(request, 'analysis.html')


def mypage(request):
    return render(request, 'mypage.html')


def login(request):
    return render(request, 'login.html')
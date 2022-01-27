from django.core.serializers import json
from django.shortcuts import render
from django.template import context


def main(request):
    tq = [1, 2, 3]
    json_tq = json.dumps(tq)

    user_rank = [
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
    ]

    json_user_rank = json.dumps(user_rank)

    context['tq'] = json_tq
    context['user_rank'] = json_user_rank

    return render(request, 'main.html', context)


def analysis(request):
    return render(request, 'analysis.html')


def mypage(request):
    return render(request, 'mypage.html')


def login(request):
    return render(request, 'login.html')
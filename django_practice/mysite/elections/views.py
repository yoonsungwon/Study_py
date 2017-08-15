# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from .models import Candidate, Poll, Choice

import datetime

# Create your views here.
def index(request):
    candidates = Candidate.objects.all()
    context = {'candidates': candidates}
    return render(request, 'elections/index.html', context)

def areas(request, area):
    today = datetime.datetime.now()
    try:
        poll = Poll.objects.get(area=area, start_date__lte=today, end_date__gte=today)  # get에 인자로 조건을 전달해줍니다.
        candidates = Candidate.objects.filter(area=area)
    except:
        poll = None
        candidates = None
    context = {'candidates': candidates,
    'area': area,
    'poll': poll,
                }
    return render(request, 'elections/area.html', context)


def polls(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    selection = request.POST['choice']
    try:
        choice = Choice.objects.get(poll_id = poll_id, candidate_id = selection)
        choice.votes += 1
        choice.save()
    except:
        choice = Choice(poll_id = poll_id, candidate_id = selection, votes = 1)
        choice.save()
    return HttpResponse("finish")
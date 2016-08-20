from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, permission_required

from charge.models import *


# Create your views here.
def index(request):

    return render_to_response('index.html',RequestContext(request,locals()))

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect('/accounts/login/')
    else:
        form = UserCreationForm
    return render_to_response('register.html',RequestContext(request,locals()))

def charge(request):
    return render_to_response('charge.html',RequestContext(request,locals()))

def missions(request):
    return render_to_response('missions.html',RequestContext(request,locals()))

def statistic(request):
    return render_to_response('statistic.html',RequestContext(request,locals()))

def battle(request):
    return render_to_response('battle.html',RequestContext(request,locals()))

def profile(request):
    return render_to_response('profile.html',RequestContext(request,locals()))

def setting(request):
    return render_to_response('setting.html',RequestContext(request,locals()))

def income(request):
    return render_to_response('income.html',RequestContext(request,locals()))

def calculator(request):
    return render_to_response('calculator.html',RequestContext(request,locals()))










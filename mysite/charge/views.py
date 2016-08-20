from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, permission_required

from charge.models import *

API_KEY = "AIzaSyBnPCKUeUkrXIxvMuYA_uikaMe4Wgaw03Q"
PKG_NAME = "com.example.wiseledger"


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
    cantback = True
    return render_to_response('charge.html',RequestContext(request,locals()))

def missions(request):
    missions = Missions.objects.filter(user_id=request.user.id)

    missionDict = {}
    for mission in missions:
        if mission.status == "processing":
            if mission.missionType == "meal":
                mis = MealMission.objects.filter(mission_id=mission.id)
                missionDict["meal"] = mis
            elif mission.missionType == "consecutivebudget":
                mis = ConsecutiveBudgetMission.objects.filter(mission_id=mission.id)
                missionDict["consecutivebudget"] = mis
            elif mission.missionType == "consecutiveconsume":
                mis = ConsecutiveConsumeMission.objects.filter(mission_id=mission.id)
                missionDict["consecutiveconsume"] = mis
            elif mission.missionType == "consecutivelogin":
                mis = ConsecutiveLoginMission.objects.filter(mission_id=mission.id)
                missionDict["consecutivelogin"] = mis
            elif mission.missionType == "random":
                mis = RandomMission.objects.filter(mission_id=mission.id)
                missionDict["random"] = mis
            else:
                print("[Warning] Unknown mission type.")
        else:
            if mission.status != "success" and mission.status != "failed":
                print("[Warning] Unknown mission status.")

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
    cantback = True
    return render_to_response('income.html',RequestContext(request,locals()))

def calculator(request, chargestate):
    if chargestate == "income":
        categoryList = Category.objects.filter(income=1)
    else:
        categoryList = Category.objects.filter(income=0)
    return render_to_response('calculator.html',RequestContext(request,locals()))

def create_record(request):
    if request.method == "POST":
        post_dict = request.POST.dict()
        print("user id = ",request.user.id)
        user = User.objects.get(id=request.user.id)
        category = Category.objects.get(name=post_dict['category'])
        record = Record(user=user,category=category,spend=post_dict['spend'],currency="NTD")
        record.save()
        print(post_dict)
        return HttpResponse("Create new record!")
    else:
        return HttpResponse("Error occured!")


def push_notify(token, title, message, postFix):
    gcm = GCM(API_KEY)
    registration_ids = [token]#"f4lCd6APSBg:APA91bHxplaOaWyL7xMoIK6vDtLNxWqjemFDaJvgtXFcYegXgD50_09lussUtR7K6NvGtdmX61qSHkiCy1a5YTG4m7wYeLoqtcN9n4HSCpEWBc2k1Gg5Yiow7qQpNndTV0SuTPE4oC0R"
    notification = {
        "title": title,
        "message": message,
        "postFix": postFix,
    }

    response = gcm.json_request(registration_ids=registration_ids,data=notification,collapse_key='awesomeapp',restricted_package_name=PKG_NAME,priority='high',delay_while_idle=False)






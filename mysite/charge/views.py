import json
import time
import datetime

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
    cantback = True

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

@login_required
def charge(request):
    sc=User.objects.filter(id=request.user.id)
    cantback = True
    if sc.count() > 0:
        user = User.objects.get(id=request.user.id)
        records = Record.objects.filter(user_id=user.id)

        recordDictList = []
        for record in records:
            if not record.category.income:
                if record.createTime.date() == datetime.datetime.now().date():
                    tempDict = {}
                    tempDict["category"] = record.category.name
                    tempDict["money"] = int(record.spend)
                    recordDictList.append(tempDict)
        recordDictList = json.dumps(recordDictList)
        return render_to_response('charge.html',RequestContext(request,locals()))
    else :
        return render_to_response('create_user.html',RequestContext(request,locals()))

@login_required
def date_changed(request, chargestate):
    if request.method == "POST":
        post_dict = request.POST.dict()
        date = datetime(post_dict["yr"],post_dict["mon"],post_dict["day"])
        user = User.objects.get(id=request.user.id)
        records = Record.objects.filter(user_id=user.id)

        recordDictList = []
        for record in records:
            if not record.category.income and chargestate=="expense" or record.category.income and chargestate=="income":
                if record.createTime.date() == date.date():
                    tempDict = {}
                    tempDict["category"] = record.category.name
                    tempDict["money"] = int(record.spend)
                    recordDictList.append(tempDict)

        print("record list = ",recordDictList)
        return HttpResponse(json.dumps(recordDictList))
    else:
        return HttpResponse("[Warning]")

@login_required
def missions(request):
    missions = Missions.objects.filter(user_id=request.user.id)

    missionDictList = []
    missionDict = {"meal":[],"consecutivebudget":[],"consecutiveconsume":[],"consecutivelogin":[],"random":[]}
    for mission in missions:
        tempDict = {}
        tempDict["status"] = mission.status
        tempDict["name"] = mission.name
        tempDict["missionType"] = mission.missionType
        missionDictList.append(tempDict)
        if mission.status == "processing":
            if mission.missionType == "meal":
                mis = MealMission.objects.filter(mission_id=mission.id)
                missionDict["meal"].extend(mis)
            elif mission.missionType == "consecutivebudget":
                mis = ConsecutiveBudgetMission.objects.filter(mission_id=mission.id)
                missionDict["consecutivebudget"].extend(mis)
            elif mission.missionType == "consecutiveconsume":
                mis = ConsecutiveConsumeMission.objects.filter(mission_id=mission.id)
                missionDict["consecutiveconsume"].extend(mis)
            elif mission.missionType == "consecutivelogin":
                mis = ConsecutiveLoginMission.objects.filter(mission_id=mission.id)
                missionDict["consecutivelogin"].extend(mis)
            elif mission.missionType == "random":
                mis = RandomMission.objects.filter(mission_id=mission.id)
                missionDict["random"].extend(mis)
            else:
                print("[Warning] Unknown mission type.")
        else:
            if mission.status != "success" and mission.status != "failed":
                print("[Warning] Unknown mission status.")

    missionDictList = json.dumps(missionDictList)
    return render_to_response('missions.html',RequestContext(request,locals()))

@login_required
def statistic(request,chargestate):

    return render_to_response('statistic.html',RequestContext(request,locals()))

@login_required
def statistic_data(request,chargestate):
    user = User.objects.get(id=request.user.id)

    if chargestate == "expense":
        categoryList = Category.objects.filter(income=0)
    elif chargestate == "income":
        categoryList = Category.objects.filter(income=1)

    categorySum = {}
    for cate in categoryList:
        categorySum[cate.name] = 0

    recordList = user.record_set.all()
    for record in recordList:
        if record.category.name in categorySum.keys():
            categorySum[record.category.name] += int(record.spend)

    dictList = []
    for cate in categorySum:
        tempDict = {}
        tempDict["name"] = cate
        tempDict["money"] = categorySum[cate]
        dictList.append(tempDict)

    print(dictList)
    return HttpResponse(json.dumps(dictList))

@login_required
def battle(request):
    user = User.objects.get(id=request.user.id)
    gender = user.gender
    dps = user.dps
    equipment = None
    _um = User_Monster.objects.get(user_id=user.id)
    monster = _um.monster
    currentHP = _um.current_hp
    createTime = _um.createTime
    exp_gain = 0
    money_gain = 0

    # calculate monster hp
    now = datetime.datetime.now()
    duration = (now-createTime).seconds
    print("seconds = ", duration)

    if duration*dps > currentHP: # defeat Boss
        exp_gain = monster.exp
        money_gain = monster.money
        monster = Monster.objects.get(id = (_um.monster.id+1)%11)
        _um.delete()
        new_um = User_Monster(user_id=user.id,monster_id=monster.id,current_hp=monster.hp,createTime=now)
        new_um.save()
        print("Defeat Boss.")

    else:
        currentHP -= duration*dps
        _um.createTime = now
        _um.current_hp = currentHP
        _um.save()
        print("Not defeat Boss.")



    return render_to_response('battle.html',RequestContext(request,locals()))

@login_required
def profile(request):
    return render_to_response('profile.html',RequestContext(request,locals()))

@login_required
def setting(request):
    return render_to_response('setting.html',RequestContext(request,locals()))

@login_required
def income(request):
    cantback = True
    user = User.objects.get(id=request.user.id)
    records = Record.objects.filter(user_id=user.id)

    recordList = []
    for record in records:
        if record.category.income:
            if record.createTime.date() == datetime.datetime.now().date():
                recordList.append(record)

    return render_to_response('income.html',RequestContext(request,locals()))

@login_required
def calculator(request, chargestate):
    if chargestate == "income":
        categoryList = Category.objects.filter(income=1)
    else:
        categoryList = Category.objects.filter(income=0)
    return render_to_response('calculator.html',RequestContext(request,locals()))

@login_required
def create_record(request):
    if request.method == "POST":
        post_dict = request.POST.dict()
        user = User.objects.get(id=request.user.id)
        category = Category.objects.get(name=post_dict['category'])
        record = Record(user=user,category=category,spend=post_dict['spend'],currency="NTD")
        record.save()
        return HttpResponse("Create new record!")
    else:
        return HttpResponse("Error occured!")

@login_required
def create_category(request):
    if request.method == "POST":
        post_dict = request.POST.dict()
        user = User.objects.get(id=request.user.id)
        category = Category(name=post_dict['name'],income=post_dict['income'])
        category.save()
        return HttpResponse("Create new category!")
    else:
        return HttpResponse("Error occured!")

@login_required
def create_user(request):
    cantback = True
    return render_to_response('create_user.html',RequestContext(request,locals()))

@login_required
def create_user_submit(request):
    if request.method == "POST":
        post_dict = request.POST.dict()
        print("user id = ",request.user.id)
        user, created = User.objects.get_or_create(id=request.user.id)
        user.gender = post_dict['gender'] == "M"
        user.facebookID = post_dict['facebookID']
        user.token = post_dict['token']
        if created :
             user.level = 0
             user.exp = 0
             user.max_exp = 100
             user.money = 0
        user.save()
        return HttpResponse("Create new User!")
    else:
        return HttpResponse("Error occured!")

@login_required
def push_notify(token, title, message, postFix):
    gcm = GCM(API_KEY)
    registration_ids = [token]#"f4lCd6APSBg:APA91bHxplaOaWyL7xMoIK6vDtLNxWqjemFDaJvgtXFcYegXgD50_09lussUtR7K6NvGtdmX61qSHkiCy1a5YTG4m7wYeLoqtcN9n4HSCpEWBc2k1Gg5Yiow7qQpNndTV0SuTPE4oC0R"
    notification = {
        "title": title,
        "message": message,
        "postFix": postFix,
    }

    response = gcm.json_request(registration_ids=registration_ids,data=notification,collapse_key='awesomeapp',restricted_package_name=PKG_NAME,priority='high',delay_while_idle=False)






# -*- coding: utf-8 -*-
from django import forms
from test_manager.models import *

#services = ((0,'Crash Testing'),(1,'Memory Leak Testing'),(2,'Coverage Based Testing'),(3,'Common Sense Testing'),(4,'Manual Testing'),(5,'Above all'),)
#versions = ((0,'4.4.2'),(1,'4.4.4'),(2,'5.0'),(3,'5.1.1'),(4,'Above All'),)
#devices = ((0,'Samsung SM-G900I'),(1,'Acer E600'),(2,'Xiaomi 2014817'),(3,'Asus ASUS_T00G'),(4,'HTC HTC_D820u'),(5,'LG LG-D855'),(6,'Sony D2203'),(7,'Google Nexus 7'),(8,'Above all'),)

services = [(s.id,s.service) for s in TestingService.objects.all()]
devices = [(d.id,d.brand+" "+d.model) for d in Device.objects.all()]
versionSet = set([d.os_version for d in Device.objects.all()]) # remove duplicated version
versions = [(AndroidVersion.objects.get(version=v).id,v) for v in versionSet]
versions = sorted(versions,key = lambda x : x[0]) # sort by version ID

absLayoutChoice = [(0,"None"),(1,"Consider Layout Only"),(2,"Ignore List View"),(3,"Ignored Classes")]
absClassesChoice = [(0,"None"),(1,"FrameLayout"),(2,"RelativeLayout"),(3,"LinearLayout"),(4,"ListView"),(5,"TextView"),(6,"ImageView"),(7,"View")]
absAttributeChoice = [(0,"None"),(1,"Set Considered Attrib"),(2,"Set Ignored Attrib")]
absAttributesChoice = [(0,"bounds"),(1,"selected"),(2,"password"),(3,"long-clickable")\
                ,(4,"scrollable"),(5,"focused"),(6,"focusable"),(7,"enabled")\
                ,(8,"clickable"),(9,"checked"),(10,"checkable"),(11,"content-desc")\
                ,(12,"package"),(13,"class"),(14,"resource-id"),(15,"text"),(16,"index")]

class UploadFileForm(forms.Form):
    service = forms.MultipleChoiceField(choices=services,label="Testing Service",required=True,widget=forms.CheckboxSelectMultiple)
    version = forms.MultipleChoiceField(choices=versions,label="Target Android Version",required=True,widget=forms.CheckboxSelectMultiple)
    device = forms.MultipleChoiceField(choices=devices,label="Target Device",required=True,widget=forms.CheckboxSelectMultiple)
    file = forms.FileField(required=True)

    def clean_file(self):
        file = self.cleaned_data["file"]
        if not file.name.endswith(".apk"):
            raise forms.ValidationError("必須上傳APK檔案")
        return file

class ProjectSettingForm(forms.Form):
    instrument = forms.ChoiceField(choices=[(0,"Yes"),(1,"No")])
    sleepTime = forms.ChoiceField(choices=[(x,x) for x in range(21)])
    absLayer = forms.ChoiceField(choices=[(x,x) for x in range(21)])
    absLayout = forms.ChoiceField(choices=absLayoutChoice)
    absIgnoredClasses = forms.MultipleChoiceField(choices=absClassesChoice,widget=forms.CheckboxSelectMultiple)
    absAttributes = forms.ChoiceField(choices=absAttributeChoice)
    absIgnoredAttrib = forms.MultipleChoiceField(choices=absAttributesChoice,widget=forms.CheckboxSelectMultiple)

    def clean_instrument(self):
        if self.cleaned_data["instrument"] == "0":
            return "yes"
        else:
            return "no"

    def clean_sleepTime(self):
        return int(self.cleaned_data["sleepTime"])

    def clean_absLayer(self):
        return int(self.cleaned_data["absLayer"])

    def clean_absLayout(self):
        if self.cleaned_data["absLayout"] == "0":
            return "None"
        elif self.cleaned_data["absLayout"] == "1":
            return "ConsiderLayoutOnly"
        elif self.cleaned_data["absLayout"] == "2":
            return "IgnoreListView"
        elif self.cleaned_data["absLayout"] == "3":
            return "IgnoredClasses"


    def clean_absIgnoredClasses(self):
        if "0" in self.cleaned_data["absIgnoredClasses"]:
            return "None"
        else:
            returnList = []
            for c in self.cleaned_data["absIgnoredClasses"]:
                for _ in absClassesChoice:
                    if c == str(_[0]):
                        if _[1] == "View":
                            returnList.append("android.view."+_[1])
                        else:
                            returnList.append("android.widget."+_[1])
            return returnList

    def clean_absAttributes(self):
        if self.cleaned_data["absAttributes"] == "0":
            return "None"
        elif self.cleaned_data["absAttributes"] == "1":
            return "setConsideredAttrib"
        elif self.cleaned_data["absAttributes"] == "2":
            return "setIgnoredAttrib"

    def clean_absIgnoredAttrib(self):
        returnList = []
        for a in self.cleaned_data["absIgnoredAttrib"]:
            for _ in absAttributesChoice:
                if a == str(_[0]):
                    returnList.append(_[1])
        return returnList




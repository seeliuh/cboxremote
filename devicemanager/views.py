# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

# from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from devicemanager.models import remotedevice

def index(request):
    return HttpResponse(u"hello world")

@csrf_exempt
def register(request):
    try:
        if request.method == 'POST':
            print("recved post")
            print(request.body)
            devicejson = json.loads(request.body)
            newdev = remotedevice()
            newdev.deviceid = devicejson['id']
            newdev.name = devicejson['name']
            newdev.ipeth0 = devicejson['ipeth0']
            newdev.ipeth1 = devicejson['ipeth1']
            newdev.internet_ip = request.META.get("REMOTE_ADDR",None)
            existdevice = remotedevice()
            try:
                existdevice = remotedevice.objects.get(deviceid=newdev.deviceid)
            except Exception as e:
                newdev.save()
            else:
                existdevice.name = devicejson['name']
                existdevice.ipeth0 = devicejson['ipeth0']
                existdevice.ipeth1 = devicejson['ipeth1']
                existdevice.internet_ip = request.META.get("REMOTE_ADDR",None)
                existdevice.save()
            finally:
                pass

        if request.method == 'GET':
            print("recved get")
    except Exception , e:
        print("cache a exception, error info:")
        print(e)
    return HttpResponse(u"register")

# Create your views here.

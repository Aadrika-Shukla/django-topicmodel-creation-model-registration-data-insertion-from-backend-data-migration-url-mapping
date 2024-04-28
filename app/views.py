from django.shortcuts import render

from django.http import HttpResponse

from app.models import *

# Create your views here.


def insert_topic(request):
    tn=input('enter topic name')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    return HttpResponse('topic is created')

def insert_Webpage(request):
    tn=input('enter topic name')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    n=input('enter name')
    u=input('enter url')
    e=input('enter email')
    WO=WebPage.objects.get_or_create(topic_name=TO,name=n,url=u,email=e)[0]
    WO.save()
    return HttpResponse('webpage is created')
    
def insert_Acess(request):
    tn=input('enter topic name')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    n=input('enter name')
    u=input('enter url')
    e=input('enter email')
    WO=WebPage.objects.get_or_create(topic_name=TO,name=n,url=u,email=e)[0]
    WO.save()
    d=input('enter date')
    a=input('enter author')
    AO=AccessRecord.objects.get_or_create(name=WO,date=d,author=a)[0]
    AO.save()
    return HttpResponse('record is created')



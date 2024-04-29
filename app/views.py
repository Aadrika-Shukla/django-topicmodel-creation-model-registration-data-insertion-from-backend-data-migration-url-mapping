from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from django.http import HttpResponse

from app.models import *


# Create your views here.


def insert_topic(request):
    tn=input('enter topic name')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    return HttpResponse('topic is created')

#creating object by using get_or_create() if it is not present in our parent table

'''def insert_Webpage(request):
    tn=input('enter topic name')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    n=input('enter name')
    u=input('enter url')
    e=input('enter email')
    WO=WebPage.objects.get_or_create(topic_name=TO,name=n,url=u,email=e)[0]
    WO.save()
    return HttpResponse('webpage is created')'''



#getting the object by get() and filter() from our parent if it is their in our parent table 

def insert_Webpage(request):
    tn=input('enter topic name')
    #TO=Topic.objects.get(topic_name=tn)
    ''' we can useget method to get the parent table object but if parent table object is not their 
    it throws doesnotexists error if you want to terminate the control flow if parent table object is not their  then use get()'''
    #TO.save() no need to save it as we are just getting the object
    n=input('enter name')
    u=input('enter url')
    e=input('enter email')
    LTO=Topic.objects.filter(topic_name=tn)
    if LTO:
        TO=LTO[0]#we need to do indexing here as filter gives list of objects so we only need object which is at 0 th index position
        WO=WebPage.objects.get_or_create(topic_name=TO,name=n,url=u,email=e)[0]
        WO.save()
        return HttpResponse('webpage is created')
    
    else:
        return HttpResponse('above given topic name is not available ,kindly give another topic name')



#creating object by using get_or_create() if it is not present in our parent table

'''   
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
'''


#getting the object by get() and filter() from our parent if it is their in our parent table 

def insert_Acess(request):
   
    n=input('enter name')
    d=input('enter date')
    a=input('enter author')
    #WO=Webpage.objects.get(name=n)
    ''' we can use get method to get the parent table object but if parent table object is not their 
    it throws doesnotexists error if you want to terminate the control flow if parent table object is not their  then use get()'''
    #WO.save() no need to save it as we are just getting the object
    LWO=WebPage.objects.filter(name=n)
    if LWO: #filter method will return queryset of list of objects(rows)
        WO=LWO[0]
        AO=AccessRecord.objects.get_or_create(name=WO,date=d,author=a)[0]
        AO.save()
        return HttpResponse('record is created')
    else:
        return HttpResponse('the above mentioned name is not their in my database')
    
    


#function to take  topic table data from database and then revert it back from backend and display that data in  form of table in frontend 

def display_topics(request):
    QLTO=Topic.objects.all()  #to take/get all the data from database where all() will return result in form of queryset of list of all objects
    d={'QLTO':QLTO}              #to send data from backend to frontend we use to send that data in form of dictionary which will be passed as an argument to context attribute
    return render(request,'display_topics.html',context=d)
    

#function to take  Webpage table data from database and then revert it back from backend and display that data in  form of table in frontend 

    

def display_Webpages(request):
    QLWO=WebPage.objects.all()   #to take/get all the data from database where all() will return result in form of queryset of list of all objects
    d={'QLWO':QLWO}              #to send data from backend to frontend we use to send that data in form of dictionary which will be passed as an argument to context attribute
    return render(request,'display_Webpages.html',context=d)
    

#function to take  AccessRecord table data from database and then revert it back from backend and display that data in  form of table in frontend 

    


def display_AccessRecords(request):
    QLAO=AccessRecord.objects.all()   #to take/get all the data from database where all() will return result in form of queryset of list of all objects
    d={'QLAO':QLAO}                    #to send data from backend to frontend we use to send that data in form of dictionary which will be passed as an argument to context attribute
    return render(request,'display_AccessRecords.html',context=d)



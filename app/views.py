from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from django.http import HttpResponse

from app.models import *


from django.db.models.functions  import Length# for arranging ordering data based on  length  of order by  function


# Create your views here.


'''
#WE ARE USING HERE GET OR CREATE METHOD INSTEAD OF USING GET() AND FILTER() BEACUSE IT IS OUR FIRST TABLE/PARENT TABLE THROUGH WHICH OTHER TABLES ARE DERIVED
def insert_topic(request):
    tn=input('enter topic name')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    return HttpResponse('topic is created')'''

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



'''#getting the object by get() and filter() from our parent if it is their in our parent table 

def insert_Webpage(request):
    tn=input('enter topic name')
    #TO=Topic.objects.get(topic_name=tn)
    #we can useget method to get the parent table object but if parent table object is not their 
    #it throws doesnotexists error if you want to terminate the control flow if parent table object is not their  then use get()
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
        return HttpResponse('above given topic name is not available ,kindly give another topic name')'''



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


'''#getting the object by get() and filter() from our parent if it is their in our parent table 

def insert_Acess(request):
   
    n=input('enter name')
    d=input('enter date')
    a=input('enter author')
    #WO=Webpage.objects.get(name=n)
    #we can use get method to get the parent table object but if parent table object is not their 
    #it throws doesnotexists error if you want to terminate the control flow if parent table object is not their  then use get()
    #WO.save() no need to save it as we are just getting the object
    LWO=WebPage.objects.filter(name=n)#always use primary key column here when your table is connected to parent table to ensure you get only unique data 
    if LWO: #filter method will return queryset of list of objects(rows)
        WO=LWO[0]
        AO=AccessRecord.objects.get_or_create(name=WO,date=d,author=a)[0]
        AO.save()
        return HttpResponse('record is created')
    else:
        return HttpResponse('the above mentioned name is not their in my database')'''
    
    


#function to take  topic table data from database and then revert it back from backend and display that data in  form of table in frontend 
# FOR WORKING OF ONE VIEW CAN RENDER MULTIPLE HTML PAGES WE SHOULD NOT COMMENT THIS DEFINING OF DISPLAY METHOS FOR ALL PAGES




'''''<ORDERING OF THE DATA BY USING ORDER_BY,USAGE OF FUNCTION  EXCLUDE TO FETCH THE DATA ,SLICING TO FETCH ONLY SPECIFIC DATA>'''
def display_topics(request):
    QLTO=Topic.objects.all()  #to take/get all the data from database where all() will return result in form of queryset of list of all objects
    
    QLTO=Topic.objects.all().order_by('topic_name')#orders topic_name coloumn according to ASCII values  in acsending order
     
    QLTO=Topic.objects.filter(topic_name='CRICKET').order_by('topic_name')#filters all CRICKET topics

    QLTO=Topic.objects.all().order_by('-topic_name')#orders topic_name coloumn according to ASCII values  in descending order  

    QLTO=Topic.objects.all().order_by(Length('topic_name'))#orders topic_name coloumn according to BASED ON LENGTH IN ASCENDING ORDER  

    QLTO=Topic.objects.all().order_by(Length('topic_name').desc())#orders topic_name coloumn according to BASED ON LENGTH IN DESCENDING ORDER

    QLTO=Topic.objects.all().exclude(topic_name='CRICKET')# IT WILL DISPLAYS ALL THE DATA EXCEPTS CRICKET
    
    QLTO=Topic.objects.all()  #to take/get all the data from database where all() will return result in form of queryset of list of all objects 




   
   
   
   
   
   
    d={'QLTO':QLTO}              #to send data from backend to frontend we use to send that data in form of dictionary which will be passed as an argument to context attribute
    return render(request,'display_topics.html',context=d)
    

#function to take  Webpage table data from database and then revert it back from backend and display that data in  form of table in frontend 

    

def display_Webpages(request):
    QLWO=WebPage.objects.all()   #to take/get all the data from database where all() will return result in form of queryset of list of all objects
    
    QLWO=WebPage.objects.all().order_by('topic_name')#orders topic_name coloumn according to ASCII values

    QLWO=WebPage.objects.filter(topic_name='CRICKET').order_by('topic_name')#filters all CRICKET topics

    QLWO=WebPage.objects.filter(topic_name='FOOTBALL').order_by('topic_name')#filters all CRICKET topics
    
    QLWO=WebPage.objects.all().order_by(Length('name'))#orders name coloumn according to BASED ON LENGTH IN ASCENDING ORDER  
    
    QLWO=WebPage.objects.all().order_by(Length('url'))#orders url coloumn according to BASED ON LENGTH IN ASCENDING ORDER  
      
    QLWO=WebPage.objects.all().order_by(Length('name').desc())#orders name coloumn according to BASED ON LENGTH IN DESCENDING ORDER  

    QLWO=WebPage.objects.filter(topic_name='FOOTBALL').order_by('name')#orders football coloumn data based on the name IN ASCENDING ORDER  
    
    QLWO=WebPage.objects.all().exclude(topic_name='FOOTBALL')#shows all the data except football
    d={'QLWO':QLWO}              #to send data from backend to frontend we use to send that data in form of dictionary which will be passed as an argument to context attribute
    return render(request,'display_Webpages.html',context=d)
    

#function to take  AccessRecord table data from database and then revert it back from backend and display that data in  form of table in frontend 

    


def display_AccessRecords(request):
    QLAO=AccessRecord.objects.all()   #to take/get all the data from database where all() will return result in form of queryset of list of all objects
    
    QLAO=AccessRecord.objects.all().order_by('date')#orders date column in ascending order
    
    QLAO=AccessRecord.objects.all().order_by('-author')#orders author column in descending order based on ascii values
    
    QLAO=AccessRecord.objects.all()[::-1]#displays data in reverse order using slicing  in list

    QLAO=AccessRecord.objects.all()[3:5:]#GET ONLY 4 AND 5 TH ID RECORD DATA

    QLAO=AccessRecord.objects.order_by(Length('name').desc())#displays data in based on length of name in descening order

    QLAO=AccessRecord.objects.filter(author='AADRIKA').order_by('id')#displays data where author id AADRIKA based on ascending order of id

    QLAO=AccessRecord.objects.exclude(author='AADRIKA')#displays data where author is not aadrika



    d={'QLAO':QLAO}                    #to send data from backend to frontend we use to send that data in form of dictionary which will be passed as an argument to context attribute
    return render(request,'display_AccessRecords.html',context=d)







#INSTEAD OF RETURNING HTTP RESPONSE WE WILL DIRECTLY RETURN HTML PAGE AS MY RESPONSE ,HENCE ONE HTML PAGE CAN BE RENDERED BY MULTIPLE VIEWS



####one html page renedered by multliple views####



#getting the object by get() and filter() from our parent if it is their in our parent table 


def insert_topic(request):
    tn=input('enter topic name')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    QLTO=Topic.objects.all()  #to take/get all the data from database where all() will return result in form of queryset of list of all objects
    d={'QLTO':QLTO}              #to send data from backend to frontend we use to send that data in form of dictionary which will be passed as an argument to context attribute
    return render(request,'display_topics.html',context=d)



####one html page renedered by multliple views####


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
        QLWO=WebPage.objects.all()   #to take/get all the data from database where all() will return result in form of queryset of list of all objects
        d={'QLWO':WebPage.objects.all()}              #to send data from backend to frontend we use to send that data in form of dictionary which will be passed as an argument to context attribute WE CAN DIRECTLY GIVE IT LIKE THIS INSTEAD OF STORING IT TO VARIBALE QLWO USE THIS   d={'QLWO':WebPage.objects.all()} OR  d={'QLWO':QLWO}
        return render(request,'display_Webpages.html',context=d)
    
    else:
        return HttpResponse('above given topic name is not available ,kindly give another topic name')
    


####one html page renedered by multliple views####


#getting the object by get() and filter() from our parent if it is their in our parent table 

def insert_Acess(request):
   
    n=input('enter name')
    d=input('enter date')
    a=input('enter author')
    #WO=Webpage.objects.get(name=n)
    ''' we can use get method to get the parent table object but if parent table object is not their 
    it throws doesnotexists error if you want to terminate the control flow if parent table object is not their  then use get()'''
    #WO.save() no need to save it as we are just getting the object
    LWO=WebPage.objects.filter(name=n)#always use primary key column here when your table is connected to parent table to ensure you get only unique data 
    if LWO: #filter method will return queryset of list of objects(rows)
        WO=LWO[0]
        AO=AccessRecord.objects.get_or_create(name=WO,date=d,author=a)[0]
        AO.save()
        QLAO=AccessRecord.objects.all()   #to take/get all the data from database where all() will return result in form of queryset of list of all objects
        d={'QLAO':QLAO}                    #to send data from backend to frontend we use to send that data in form of dictionary which will be passed as an argument to context attribute
        return render(request,'display_AccessRecords.html',context=d)
    else:
        return HttpResponse('the above mentioned name is not their in my database')




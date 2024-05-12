from django.shortcuts import render

# Create your views here.
from app.models import *
from django.db.models import Q







'''##########---- logical operator in orm#######
-----> for and you can just use , comma between 2 queries to perform and operations else you can use & symbol also

------>for using or operator  as or operator means concatenation  of 2 or more querysets which means querysets of list of multiple objects
so you can't directly use |(parellel pipe symbol for or operation directly here)so first you need 
to convert the querysets into queryobject so that you can perform concatenation(+)/or operation between 2 objects
for thta you need to import Q (queryobject) from django.db.models import Q.

------>1) when you are writing a query using both or , and operators then you need to use & symbol here for 
performing and operation ;
       2) in this case your and as well as or operator query must be written with using Q(or operator query)&Q(and operator query)

------>for using not operator we have exclude() operator with us-that gives all the data except what we pass as agrument
       to exclude
'''







def logicaloperators(request):


    #fetching data using and(,),(|)or operator,exclude (not) from our table

    JDED=Emp.objects.select_related('deptno').all()
    JDED=Emp.objects.select_related('deptno').filter(Q(job='SALESMAN')|Q(deptno=30))
    JDED=Emp.objects.select_related('deptno').filter(job='SALESMAN',deptno=30)
    JDED=Emp.objects.select_related('deptno').filter(hiredate__year__lt=1982,sal__gt=2500)
    JDED=Emp.objects.select_related('deptno').filter(hiredate__year__lte=1982,deptno=30,sal__lte=1500)
    JDED=Emp.objects.select_related('deptno').filter((Q(ename__startswith='a')|Q(ename__endswith='n')|Q(ename__endswith='s'))&Q(deptno=30))
    JDED=Emp.objects.select_related('deptno').filter(sal__gte=2000,deptno=20)
    JDED=Emp.objects.select_related('deptno').filter(hiredate__year__gt=1982,job='ANALYST')
    JDED=Emp.objects.select_related('deptno').exclude(job='PRESIDENT')


    d={'JDED':JDED}
    return render(request,'logicaloperators.html',d)







''''for performing joins in orm we have two methods-i)select_related-used when one to one ,many to one relationship is their
ii)prefetch-related---used when we have many to many,one to many relationship is their'''






def innerEquijoins(request):
    JDED=Emp.objects.select_related('deptno').all()

    #fetching data usng select_related using innner equi joins
    JDED=Emp.objects.select_related('deptno').filter(job='CLERK')
    JDED=Emp.objects.select_related('deptno').filter(Q(job='SALESMAN')|Q(deptno=30))
    JDED=Emp.objects.select_related('deptno').filter(job='SALESMAN',deptno=30)
    JDED=Emp.objects.select_related('deptno').filter(mgr=7839)
    JDED=Emp.objects.select_related('deptno').filter(hiredate__year__lt=1982)
    JDED=Emp.objects.select_related('deptno').filter(sal__gte=3000)
    JDED=Emp.objects.select_related('deptno').filter(hiredate__year__lt=1982,sal__gt=2500)
    JDED=Emp.objects.select_related('deptno').filter(hiredate__year__lte=1982,deptno=30,sal__lte=1500)
    JDED=Emp.objects.select_related('deptno').filter(comm=0)
    JDED=Emp.objects.select_related('deptno').filter((Q(ename__startswith='a')|Q(ename__endswith='n')|Q(ename__endswith='s'))&Q(deptno=30))
    JDED=Emp.objects.select_related('deptno').filter(hiredate__day__lt=28)
    JDED=Emp.objects.select_related('deptno').filter(sal__gte=2000,deptno=20)
    JDED=Emp.objects.select_related('deptno').filter(hiredate__year__gt=1982,job='ANALYST')
    JDED=Emp.objects.select_related('deptno').filter(sal__lt=3000)
    JDED=Emp.objects.select_related('deptno').filter(empno__gte=7500)
    JDED=Emp.objects.select_related('deptno').filter(deptno__dname='RESEARCH')# AS DNAME IS PRESENT IN OUR DEPT TABLE SO WE CAN ACCESS DATA BY COMMONCOLOUMNNAME__COLUMNNAME=VALUE
    

    


    d={'JDED':JDED}
    return render(request,'innerEquijoins.html',d)








def innerselfjoins(request):
    JDEM=Emp.objects.select_related('mgr').all()

    #fetching data usng select_related using innner self joins


    JDEM=Emp.objects.select_related('mgr').filter(mgr__ename='BLAKE')
    JDEM=Emp.objects.select_related('mgr').filter(Q(mgr__ename='BLAKE')|Q(mgr__ename='CLARK'))
    JDEM=Emp.objects.select_related('mgr').filter(mgr__ename__startswith='F')
    JDEM=Emp.objects.select_related('mgr').filter(mgr__deptno=30)
    JDEM=Emp.objects.select_related('mgr').filter(mgr__deptno=30,sal__gt=1500)
    JDEM=Emp.objects.select_related('mgr').filter(mgr__deptno=20,hiredate__year__gt=1981)
    JDEM=Emp.objects.select_related('mgr').filter(job='CLERK',mgr__sal__gte=2500)
    JDEM=Emp.objects.select_related('mgr').filter(comm__isnull=False)
    JDEM=Emp.objects.select_related('mgr').filter(job='SALESMAN',mgr__sal__gte=1200)
    JDEM=Emp.objects.select_related('mgr').filter(mgr__ename='KING')
    #JDEM=Emp.objects.select_related('mgr').filter((mgr__deptno)__IN=(Emp.objects.select_related('mgr').filter(deptno=10)))#here subqueries will be used
   
    JDEM=Emp.objects.select_related('mgr').filter(mgr__ename__in=['FORD','KING'])
    JDEM=Emp.objects.select_related('mgr').filter(sal__gte=1500,mgr__ename__contains='a')
    JDEM=Emp.objects.select_related('mgr').filter(mgr__deptno=10) 
    JDEM=Emp.objects.select_related('mgr').filter(mgr__ename__in=['FORD','KING'])
    JDEM=Emp.objects.select_related('mgr').filter(mgr__deptno__in=(20,30))
    
    JDEM=Emp.objects.select_related('mgr').filter(mgr__hiredate__year__in={1981,1982})


    d={'JDEM':JDEM}
    return render(request,'innerselfjoins.html',d)







''''JOINING MORE THAN 2 TABLES  IN OUR ORM IN SQL WE NEED TO MENTION TABLE NAME FOR JOINING THE TABLES BUT IN OUR ORM WE JUST
NEED TO MENTION OUR COMMON  COLUMN NAMES AND MY ORM WILL SEARCH FOR THAT FOREIGN KEY COLUMN AND JOINED THAT TABLE BY ITSELF'''

#####use of extra() to wrie raw sql queries in case of complex operations#####





def multitablejoins(request):
    JDEMD=Emp.objects.select_related('deptno','mgr').all()#we are using select_related because that mgr and dept no are foreign key

    JDEMD=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='BLAKE',deptno__loc='CHICAGO')

    JDEMD=Emp.objects.select_related('deptno','mgr').filter(mgr__sal__gt=2000,deptno__loc__in={'CHICAGO','DALLAS'})

    JDEMD=Emp.objects.select_related('deptno','mgr').filter(mgr__sal__gt=2000,deptno__loc__in={'CHICAGO','DALLAS'},ename__contains='s')

    JDEMD=Emp.objects.select_related('deptno','mgr').filter(sal__gt=2000,deptno__dname__in={'RESEARCH','SALES'})# FOR SEARCHING DATA OF JOINED TABLE YOU SHOULD GIVE:COMMONCOLOUMN NAME__COLUMNNAME='VALUE'

    #JDEMD=Emp.objects.select_related('deptno','mgr').filter(sal__gt=2000,deptno__dname='RESEARCH',mgr__deptno='RESEARCH')# FOR SEARCHING DATA OF JOINED TABLE YOU SHOULD GIVE:COMMONCOLOUMN NAME__COLUMNNAME='VALUE'

   
    ''''#######--------TO EXECUTE TASK LIKE ONLY SPECIFIC CHARACTERS MATCHING WE HAVE TO USE CONCEPT OF ANNOTATIONS
,SO INSTEAD OF DOING THAT WE CAN USE THE CONCEPT OF RAW SQL QUERIES FOR WRITING RAW SQL QUERIES WE NEED TO USE EXTRA()
WHICH WILL TAKE 1 ARGUMENT WHERE=[''] ,IN WHERE WE NEED TO WRITE THE CONDITION  IN FORM OF STRINGS,
THEIR SHOULD BE SPACE BETWEEN = AND QUERY ELSE IT WILL NOT EXECUTE AND SHOW YOU THE RESULT
raw sql  -> means normal sql query
'''
     
    ########---------USING EXTRA () TO WRITE RAW SQL QUESRIES--------#########


    JDEMD=Emp.objects.extra(where=['LENGTH(ename) = 5'])  #it will fetch details of employee having name containing only 5 characters

    JDEMD=Emp.objects.extra(where=['LENGTH(ename) IN (SELECT dname FROM Dept where LENGTH(dname) = 5)'])

    JDEMD=Emp.objects.extra(where=["ename LIKE  '%E_' "]) # FETCHES DETAILS HAVING LAST 2ND CHARATER IS E IN NAME

    JDEMD=Emp.objects.extra(where=['LENGTH(ename) = 5 AND LENGTH(job) = 5']) 




    
    d={'JDEMD':JDEMD}
    return render(request,'multitablejoins.html',d)








''''FOR DOING SUBQUERIES RELATED TASK WE WILL USE VALUES() TO FETCH ONLY SPECIFIC OBJECTS WHERE TABLE IS NOT CONNECTED DIRECTLY IN DJANGO WE WILL MOVE TO CONCEPT OF ANNOTATIONS INSTEAD OF USING ANNOTATIONS WE WILL MOVE FOR
WARD WITH THE CONCEPT OF VALUES()-WHICH WILL RETURN ONLY THAT QUERY OBJECT THAT IS PASSED AS AN ARGUMENT TO VALUE'''


def subqueries(request):
    
    #emp dept salgrade join data #no foreign keys so can't display salgrades losal and hisal coloumns  in  frontend so use shell in order to verify the results 

    EMSJD=Emp.objects.select_related('deptno','mgr').all()#we are using select_related because that mgr and dept no are foreign key

    EMSJD=Emp.objects.values('ename','sal').filter(sal__gt=Salgrade.objects.values('losal').filter(grade=1),sal__lt=Salgrade.objects.values('hisal').filter(grade=1))
    
    #output ->   <QuerySet [{'ename': 'SMITH', 'sal': Decimal('800.00')}, {'ename': 'ADAMS', 'sal': Decimal('1100.00')}, {'ename': 'JAMES', 'sal': Decimal('950.00')}]>

    EMSJD=Emp.objects.values('ename','sal').filter(sal__gt=Salgrade.objects.values('losal').filter(grade=2),sal__lt=Salgrade.objects.values('hisal').filter(grade=2))

    #output ->     <QuerySet [{'ename': 'WARD', 'sal': Decimal('1250.00')}, {'ename': 'MARTIN', 'sal': Decimal('1250.00')}, {'ename': 'MILLER', 'sal': Decimal('1300.00')}]>

    EMSJD=Emp.objects.values('ename','sal').filter(sal__gt=Salgrade.objects.values('losal').filter(grade=3),sal__lt=Salgrade.objects.values('hisal').filter(grade=3))
    
    #output  ->     <QuerySet [{'ename': 'ALLEN', 'sal': Decimal('1600.00')}, {'ename': 'TURNER', 'sal': Decimal('1500.00')}]>


    EMSJD=Emp.objects.values('ename','sal').filter(sal__gt=Salgrade.objects.values('losal').filter(grade=4),sal__lt=Salgrade.objects.values('hisal').filter(grade=4))

    #output    ->    <QuerySet [{'ename': 'JONES', 'sal': Decimal('2975.00')}, {'ename': 'BLAKE', 'sal': Decimal('2850.00')}, {'ename': 'CLARK', 'sal': Decimal('2450.00')}]>


    EMSJD=Emp.objects.values('ename','sal').filter(sal__gt=Salgrade.objects.values('losal').filter(grade=5),sal__lt=Salgrade.objects.values('hisal').filter(grade=5))

    #output     ->    <QuerySet [{'ename': 'KING', 'sal': Decimal('5000.00')}]>

    EMSJD=Emp.objects.select_related('deptno','mgr').all()

    d={'EMSJD':EMSJD}

    return render(request,'subqueries.html',d)









'''updating the table data using update() and update_or_create() for updating the data first write 
updating condition then render the html page and display details in frontend
for update() you can use filter() as well as all() but for update_or_create() you no neeed to use any method for filtering the records
for both the methods we don't need to give variable to store the objects
in sql udpate and insert were dml commands hence temporary chnages but here in orm update is permanent command
in update_or_create() column you want to update must be given as dictionary to defaults where key will be column name
and value will be update value and conditions returned before defaults are filtering conditions beacuse we are
not using here filter() '''











def update_table(request):


    #---------USING UPDATE() TO UPDATE OUR DATA

    UDE=Emp.objects.all()


    #Emp.objects.all().update(columnname=value)   #used to update all the rows of data with new values


    Emp.objects.filter(comm=None).update(comm=0)# multi rows satisfies updates it

    Emp.objects.filter(ename='KING').update(comm=1000000)# SINGLE row satisfies updates it

    Emp.objects.filter(ename='AADRIKA').update(sal=1000000)# no row so no  updation done here

    ####---Emp.objects.filter(ename='KING').update(deptno=1000000)# for foriegn key column data you are trying to update must me present in our parent table(from which foriegn key connections is done) so it will throw INTEGRITY ERROR

    Emp.objects.filter(ename='KING').update(deptno=40)  # as this deptno 40 was present in our parent table so it get updated here

    Emp.objects.filter(ename='KING').update(deptno=40,sal=10000) #you can update as many column you want to update as well as you can pass multiple column name for filter() here.



    #---------           USING UPDATE_OR_CREATE()   --------#





    #Emp.objects.update_or_create(comm=0,defaults={'comm':None}) # satisfying multiple rows so it will throw error as MultipleObjectsReturned as update_or_create can only work with single row data 

    Emp.objects.update_or_create(ename='KING',defaults={'comm':10000})# SINGLE row satisfies updates it

    Emp.objects.update_or_create(ename='KING',defaults={'sal':500000})

    #Emp.objects.update_or_create(ename='AADRIKA',defaults={'sal':1000000})# AS NO DATA EName =aadrika is present so update_or_create() will create a new row for that you need to give data/value for every column
     

    '''1)as we need to create a new object/row to the table which is not present in our table 
    we need to get the object of our parent table in order to update it 
    2)WE NEED TO PROVIDE EVERY COLUMN DATA/VALUE  WE ARE GOING TO CREATE(NEW RECORD/ROW/OBJECT)'''

    DO=Dept.objects.get(deptno=40,dname='OPERATIONS',loc='BOSTON')
    MO=Emp.objects.get(empno=7839)#AS I NEED TO GET THE DETAILS OF KING AS EMPLOYEE WILL WORK UNDER EVERY REPORTING MANAGER
    
    Emp.objects.update_or_create(ename='AADRIKA',defaults={'empno':5555,'job':'DATA ANALYST','hiredate':'2001-04-19','comm':0,'sal':1000000,'deptno':DO,'mgr':MO})

    
        
    d={'UDE':UDE}
    return render(request,'updateddata.html',d)













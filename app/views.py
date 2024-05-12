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














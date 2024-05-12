from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Emp(models.Model):
    empno=models.IntegerField(max_length=4,primary_key=True)
    ename=models.CharField(max_length=10)
    hiredate=models.DateField()
    mgr=models.ForeignKey('self',on_delete=models.SET_NULL,null=True,blank=True)

    '''1)we used here on_delete=models.setnull beacause if we delete parent data it should not delete respective
    child because if manager resigned only his data should be deleted not all the employees working under that manager
    should get delete ,2)we have used self/Emp here because their is one to many relatonship between mgr and emp table as 
     one manager(mgr) is assigned to many employees(empno) ,3)null=true because when we are inserting a new data it have null value and some employee are having 
    null(no one) as his reportingmanager(mgr),4)we have taken blank=true as it is part of frontend or form field so that it should 
    take the data from forms'''
    job=models.CharField(max_length=20 )
    deptno=models.ForeignKey('Dept',on_delete=models.CASCADE)
    sal=models.DecimalField(max_digits=10,decimal_places=2)
    # or we can take sal=models.IntegerField()
    comm=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    # number=12345678.90 max_digits=all the digits count and decimal places=from right end 2 places or 2 decimal floating point number


    def __str__ (self):
        return self.ename




class Dept(models.Model):
    deptno=models.IntegerField(max_length=2,primary_key=True)
    dname=models.CharField(max_length=10,unique=True)
    
    # as dept name will be unique only so that out table should not create same data entry for same dept name
    loc=models.CharField(max_length=10)


    def __str__(self):
        return str(self.deptno)

class Salgrade(models.Model):
    grade=models.IntegerField(max_length=4,primary_key=True)
    losal=models.IntegerField(max_length=4)
    #or losal=models.DecimalField(max_digits=10,decimal_places=2)
    hisal=models.IntegerField(max_length=4)
    #or hisal=models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return str(self.grade)






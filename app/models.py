from django.db import models

# Create your models here.




# Create your models here.
class Topic(models.Model):
    topic_name=models.CharField(max_length=100,primary_key=True)
    #email=models.EmailField(default='abc@gmail.com')
    def __str__(self):
        return self.topic_name
    

class WebPage(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    url=models.URLField()
    email=models.EmailField(default='abc@gmail.com')
    def __str__(self):
        return self.name


class AccessRecord(models.Model):
    name=models.ForeignKey(WebPage,on_delete=models.CASCADE)
    date=models.DateField()
    author=models.CharField(max_length=100)
    #editorial=models.CharField(max_length=100,default='xyz')

    def __str__(self):
        return self.author




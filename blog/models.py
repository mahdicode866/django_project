from django.db import models
from django.contrib.auth.models import User
# Create your models here. -> ok brother i want it to 

class post(models.Model):
    image=models.ImageField(upload_to="blog/",default="\blog\default.jpg")
    author=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    title=models.CharField(max_length=255)
    content=models.TextField()
    # tag
    # category
    counted_views=models.IntegerField(default=0)
    status=models.BooleanField(default=False)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)      
    published_date=models.DateTimeField(null=True)
    


    def __str__(self) :
     #     return (f"{self.title}{self.id}")
     return "{} -{}".format(self.title,self.id)

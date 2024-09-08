from django.db import models

# Create your models here. -> ok brother i want it to 

class post(models.Model):
     # image
    # author 
    title=models.CharField(max_length=255)
    content=models.TextField()
    # tag
    # category
    counted_views=models.IntegerField(default=0)
    status=models.BooleanField(default=False)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)      
    published_date=models.DateTimeField(null=True)
     
    
    class Meta:
         
         ordering=["created_date",]
         verbose_name="post"
         verbose_name_plural="posts"

#     def __str__(self) :
#      #     return (f"{self.title}{self.id}")
#      return "{} -{}".format(self.title,self.id)


# ////

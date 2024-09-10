from django.http import HttpResponse
from django.urls  import path
from . import views


app_name="blog"
urlpatterns=[
    
    path('',views.blog,name='index'),
    path('<int:pid>',views.single,name='single'),
    path("test",views.test)
]
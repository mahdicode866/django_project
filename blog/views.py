from django.shortcuts import render,get_object_or_404
from blog.models import post
from django.http import HttpResponse
# Create your views here.

def blog(request):
    mydata=post.objects.filter(status=1)
    context={"mydata":mydata}
    return render(request,"blog/blog-home.html",context=context)

def single(request,pid):
    mydata=get_object_or_404(post,pk=pid)
    context={"mydata":mydata}
    return render(request,"blog/blog-single.html",context=context)

def test(request,pid):
    # mydata=get_object_or_404(post,pk=pid)
    # context={"mydata":mydata}
    return render(request,"test.html")
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def blog(request):
    return render(request,"blog/blog-home.html")

def single(request):
    return render(request,"blog/blog-single.html")
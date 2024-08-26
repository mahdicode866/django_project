from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

# def hello(request):
#     return render(request,'index.html')



# def hello(request):
    # temp=loader.get_template('index.html')
    # return HttpResponse(temp.render())
    
    
# def hello(request):
#     temp=loader.get_template('index.html')
#     return HttpResponse(temp.render())


# def hello (request):
#     return render(request,'index.html')
def hello(request):
    return render(request,'website/index.html')
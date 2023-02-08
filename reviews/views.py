from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.

def review(request):
    if request.method=='POST': #checking the  HTTP method
        entered_username = request.POST['username']
        return HttpResponseRedirect('thank-you')
    return render(request,"reviews/index.html")

def thankyou(request):
    return render(request,'reviews/thankyou.html')
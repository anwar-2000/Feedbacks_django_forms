from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.

from .forms import reviwForm

def review(request):
    if request.method=='POST': #checking the  HTTP method
        form = reviwForm(request.POST)
        if form.is_valid(): #if we dont get the cleaned data then , create a form again 
           print(form.cleaned_data)  
           return HttpResponseRedirect('/thank-you') 
    else :
         form = reviwForm() #intitiat the form if not received data

    return render(request,"reviews/index.html",
    {"form" : form})

def thankyou(request):
    return render(request,'reviews/thankyou.html')
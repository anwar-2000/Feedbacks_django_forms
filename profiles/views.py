from django.shortcuts import render
from django.views import View 
from django.views.generic import CreateView , ListView
from django.http import HttpResponseRedirect


#from .forms import ProfileForm

from .models import UserProfile
# Create your views here.

class createProfileView(CreateView):
    template_name="profiles/create_profile.html"
    model = UserProfile
    fields="__all__"
    success_url="/profiles"

class userProfiles(ListView):
    template_name="profiles/user_profile.html"
    model = UserProfile
    context_object_name="profiles"

#def storeFile(file):
  #  with open("temp/image.png","wb+") as dest:
     #   for chunk in file.chunks():
     #       dest.write(chunk)

#class CreateProfileView(View):
    #def get(self, request):
       # form = ProfileForm()
      #  return render(request, "profiles/create_profile.html",{
       #     "form" : form
       # })

   # def post(self, request):
    #    subbmittedForm = ProfileForm(request.POST,request.FILES)

     #   if(subbmittedForm.is_valid()):
      #      profile = UserProfile(image=request.FILES["user_image"])
      #      profile.save()
      #      return HttpResponseRedirect('/profiles')
      #  return render(request,"profiles/create_profile.html",{
      #      "form" : subbmittedForm
     #   })
#
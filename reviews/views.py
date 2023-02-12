from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View 
from django.views.generic.base import TemplateView
from django.views.generic import ListView , DetailView
from django.views.generic.edit import FormView , CreateView
# Create your views here.

from .forms import ReviewForm


from .models import Reviews


class ReviewView(CreateView):
    model = Reviews
    form_class = ReviewForm
    template_name="reviews/index.html"
    success_url = "/thank-you"

   # def form_valid(self, form) :  # because now createview will send data automatically
   #     form.save()
   # #    return super().form_valid(form)

  #  def get(self,request): #if HTTP method is GET
       #  form = ReviewForm() #intitiat the form if not received data
       #  return render(request,"reviews/index.html",
  #  {"form" : form})

    #def post(self,request):  #if HTTP method is POST
   #      form = ReviewForm(request.POST)
    #     if form.is_valid(): #if we dont get the cleaned data then , create a form again 
     #      form.save()  #better method when using modelForm
     #      return HttpResponseRedirect('/thank-you') 

     #    return render(request,"reviews/index.html",
  #  {"form" : form})
     

class thankYouView(View):
    def get(self,request):
        return render(request,'reviews/thankyou.html')

class ReviewsListView(ListView):
    template_name="reviews/reviews_list.html"
    model = Reviews
    context_object_name="reviews"
    #def get_context_data(self, **kwargs):
       # context =  super().get_context_data(**kwargs)
      #  reviews = Reviews.objects.all()
      #  context['reviews'] = reviews

      #  return context

class Review_detail(DetailView):
    template_name="reviews/reviewDetail.html"
    model = Reviews

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_item = self.object #get the loaded item in the detail page
        request = self.request #get the request of it
        favorite_id =  request.session["favorite_review"]
        context["is_favorite"] = favorite_id == str(loaded_item.id) #true if its the favorite
        return context


   # def get_context_data(self, **kwargs):
    #    context = super().get_context_data(**kwargs)
    #    review_id = kwargs['id']
    #    review = Reviews.objects.get(pk=review_id)
    #    context['review'] = review
    #    return context
       
class AddFavoriteView(View):
    def post(self,request):
        review_id = request.POST['review__id']
        #favoriteReview = Reviews.objects.get(pk=review_id)#this will return an object and we can't pass it as session object
        request.session["favorite_review"] = review_id #pass it as a string
        return HttpResponseRedirect("/reviews/"+review_id)
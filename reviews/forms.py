from django import forms 
from .models import Reviews
#class reviwForm(forms.Form):
   # user_name = forms.CharField(label="Username" , max_length=100,error_messages={"required" : "Your name must not be empty ! ","max_length" : "Please enter a shorter name!"})
   # review_text = forms.CharField(widget=forms.Textarea, label="Your Feedback",max_length=200)
   # rating = forms.IntegerField(max_value=5 , min_value=1 , label="Your Rating")

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews 
        fields ="__all__"
       # exclude = ['rating']
        labels={
        "username" : "Your Name",
        "feedback" : "Your Feedback",
        "rating" : "Your Rating"
       }
        error_messages = {
        "username" : {
            "required" :"Your name must not be empty!",
            "max_length" : "Please enter a shorter name!"
        },
        "feedback" : {
            "required" :"Your feedback must not be empty!",
            "max_length" : "Please enter a shorter feedback!"
        }
       }

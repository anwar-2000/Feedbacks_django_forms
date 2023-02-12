from django.urls import path

from . import views

urlpatterns = [
    path("",views.ReviewView.as_view()),
    path("thank-you",views.thankYouView.as_view()),
    path("reviews",views.ReviewsListView.as_view()),
    path("reviews/favorite",views.AddFavoriteView.as_view()),#before the last path so django wont be confused and make it seems that favorite is a PK
    path("reviews/<int:pk>",views.Review_detail.as_view())
]

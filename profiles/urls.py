from django.urls import path

from . import views

urlpatterns = [
    path("", views.createProfileView.as_view()),
    path("list",views.userProfiles.as_view())
]

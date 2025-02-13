from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('editprofile/',views.edit_profile,name="edit_profile"),
]
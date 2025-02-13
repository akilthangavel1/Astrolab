from django.urls import path
from . import views

urlpatterns = [
    path('', views.jyotishmatch, name="jyotishmatch"),
    path('ajax/add_person/', views.ajax_add_person, name="addperson"),
    path('ajax/validate_person_name/', views.ajax_validate_person_name, name="vperson"),
    path('ajax/validate_person_name_admin/', views.ajax_validate_person_name_admin, name="vadminperson"),

]
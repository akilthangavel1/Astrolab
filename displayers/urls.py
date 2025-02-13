from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_one, name="displayOne"),
    path('displaytwo/', views.display_two, name="displayTwo"),
    path('displaythree/', views.display_three, name="displayThree"),
    path('displayhouses/', views.display_houses, name="displayHouses"),
    path('astrotables/', views.astro_tables, name="astroTables"),
]
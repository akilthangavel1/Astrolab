from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_main, name="homemain"),
    path("p2phome", views.p2pform, name="p2phome"),
    path("nchart/", views.natalform, name="nchart"),
    path("nchartlink/", views.nchartlink, name="nchartlink"),
    path("p1form/", views.p1form, name="p1home"),
    path("p1xp2exform/", views.p1xp2exactform, name="p1xp2exform"),
    path("axreportform/", views.ax_report_form, name="axhome"),
    path("irform/", views.ir_form, name="ir_form"),
    path("pdfrender/", views.donation_receipt, name="render_pdf"),
    path("maptesting/", views.maps_home, name="maptesting"),
    path("maptesting1/", views.maps_home1, name="maptesting1"),
    path("homedegree/", views.home_degree, name="homedegree"),
    path("homedegree1/", views.home_degree1, name="homedegree1"),
    path("impeoples/", views.impeople, name="impeoples"),
    path('impeopleedit/<id>/', views.impeopleedit, name="impeopleedit"),
    path('impeopledelete/<int:id>', views.destroy, name="impeopledelete"),
    
]
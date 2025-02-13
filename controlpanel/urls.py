from django.urls import path
from . import views
from .multiple2 import multiple_rangeft, multiple_sdate, multiple_weekdays, multiple_rangeyear, mclear, mresult
from .multiple3 import result_category_graph



urlpatterns = [
    path('', views.exaspecthome, name="exaspecthome"),
    path('multiple2/', views.multiple2home, name= "multiple2home"),
    path('multiple2fromto/',multiple_rangeft , name= "multiple_rangeft"),
    path('multiple_sdate/',multiple_sdate , name= "multiple_sdate"),
    path('multiple_weekdays/',multiple_weekdays , name= "multiple_weekdays"),
    path('multiple_rangeyear/',multiple_rangeyear , name= "multiple_rangeyear"),
    path('mresult/',mresult , name= "mresult"),
    path('mclear/',mclear , name= "mclear"),
    path('peekmultiple/', views.peekmultipledays, name= "peekmultiple"),
    path('peekclear/', views.peekclearfun, name= "peekclear"),
    path('peekmultipleplanets/', views.peekmultipleplanets, name= "peekmultipleplanets"),
    path('addsingle/', views.addsingledate, name= "addsingle"),
    path('weekcheckers/', views.weekcheckers, name= "weekcheckers"),
    path('specificdyears/', views.specificdyears, name= "specificdyears"),
    path('pointsHome/', views.pointsHome, name= "pointsHome"),
    path('pointsEdit/<id>/', views.pointsEdit, name="pointsEdit"),
    path('pointsDelete/<int:id>', views.pointsDelete, name="pointsDelete"),
    path('cptest/', views.cpTest, name="cpTest"),
    path('wchanger/', views.wchanger, name="wchanger"),
    path('multiplecategoryhome/', views.multiple_category_home, name="multipleCategoryHome"),
    path('multiplecategorylist/', views.multiple_category_list, name="multipleCategoryList"),
    path('multiplecategorylist/multiplecategoryedit/<id>/', views.multiple_category_edit, name="multipleCategoryEdit"),
    path('multiplecategorylist/multiplecategorydelete/<int:id>', views.multiple_category_delete, name="multiplecategorydelete"),
    path('resultcategorygraph/', result_category_graph, name="resultCategoryGraph"),
    path('multicategories/', views.multiple_categories, name="multicategories"),
    path('addcategory/', views.add_category, name="addCategory"),
    path('addpeoplecategory/', views.add_people_category, name="addpeoplecategory"),
    path('multicategoriesdivin/', views.add_multiple_category_division, name="addMultipleCategoryDivision"),
    path('trendchartshome/', views.trend_charts_home, name="trendChartsHome"),
    path('trendchartsview/', views.trend_chart_view, name="trendChartView"),
    path('trendchartsview/trendchartsedit/<id>/', views.trend_chart_edit, name="trendChartEdit"),
    path('trendchartsview/trendchartsdelete/<int:id>', views.trend_chart_delete, name="trendChartDelete"),
    path('getgroupchanger/', views.getgc_home, name="getgcHome"),
    path('planetgroupernameadd/', views.planet_grouper_name_add, name="planetGrouperNameAdd"),
    path('planetgrouperadd/', views.planet_grouper_add, name="planetGrouperAdd"),
    path('planetgrouperview/', views.planet_grouper_view, name="planetGrouperView"),
    path('planetgrouperview/planetgrouperupdate/<id>/', views.planet_grouper_update, name="planetGrouperUpdate"),
    path('planetgrouperview/planetgrouperdelete/<int:id>', views.planet_grouper_delete, name="planetGrouperDelete"),
]



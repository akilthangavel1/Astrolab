from django.conf.urls import include
from django.urls import path
from match import views

#

urlpatterns = [
    path('', views.HomePageView.as_view()),
    path('index', views.HomePageView.as_view()),
    path('relocation_map_input', views.RelocationMap3dInputView.as_view(), name="reinput"),
    path('relocation_map3d', views.RelocationMap3dView.as_view()),
    path('ajax/validate_person_name/', views.ajax_validate_person_name, name="vperson"),
    path('ajax/validate_person_name_admin/', views.ajax_validate_person_name_admin, name="vpersonadmin"), 
    path('ajax/add_person/', views.ajax_add_person, name="addperson"),
    path('ajax/save_labels/', views.ajax_save_labels, name="slabels"),
    path('ajax/save_session/', views.ajax_save_session),
    path('ajax/delete_session/', views.ajax_delete_session),
    path('ajax/delete_user/', views.ajax_delete_user),
    path('ajax/delete_user_video_link/', views.delete_user_video_link),
    path('ajax/add_user_video_link/', views.add_user_video_link),
    path('ajax/add_user_video_link/', views.add_user_video_link),
    path('ajax/save_video_link/', views.save_video_link), 
    path('ajax/edit_video_links/', views.edit_video_links),
    path('ajax/get_degrees/', views.get_degrees, name="getdegree") 
]

from django.urls import path
# from match import views
from . import views

urlpatterns = [
    path('relocation_map_input', views.RelocationMap3dInputView.as_view(), name="reinput"),
    path('relocation_map3d', views.RelocationMap3dView.as_view(), name='relocation_map3d'),
    path('maplatest/add_person/', views.maplatest_add_person, name="addperson"),
    path('maplatest/save_labels_maps/', views.ajax_save_labels_map, name="maplatestslabels"),
    path('autocomplete/', views.autocomplete_names, name='autocomplete-names'),
]

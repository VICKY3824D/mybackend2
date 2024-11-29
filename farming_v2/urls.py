from django.urls import path
from farming_v2 import views

urlpatterns = [
    path('petani/', views.petani_list),
    path('tanaman/', views.tanaman_list),
    path('panenan/', views.panenan_list),
    path('petani/<int:pk>/', views.petani_detail),
    path('tanaman/<int:pk>/', views.tanaman_detail),
    path('panenan/<int:pk>/', views.panenan_detail),
    
]


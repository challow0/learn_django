from django.urls import path,re_path
from . import views

urlpatterns = [

    # /music/
    path('', views.index, name='index'),

    # /music/71/
    re_path('(\d+)/', views.detail,name='detail'),
]
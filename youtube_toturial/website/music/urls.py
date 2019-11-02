from django.urls import path,re_path
from . import views

app_name = 'music'

urlpatterns = [

    # # /music/
    # path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='index'),

    # /music/<album_id>/
    # re_path('(\d+)/', views.detail,name='detail'),
    re_path(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # # /music/<album_id>/
    # re_path('(\d+)/favorite/', views.favorite,name='favorite'),
    # /music/album/add/
    re_path(r'album/add/$', views.AlbumCreate.as_view(), name = 'album-add'),
]
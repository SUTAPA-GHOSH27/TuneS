
from django.urls import path 
from . import views


urlpatterns = [
    path('songs', views.songs, name='songs'),
    path('songs/<int:id>', views.songpost, name='songpost'),
    path('login', views.user_login, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout', views.user_logout, name='logout'),
    path('watchlater', views.watchlater, name='watchlater'),
    path('search', views.search, name='search'),
    path('add_to_watchlater', views.add_to_watchlater, name='add_to_watchlater'),
    path('remove_from_watchlater', views.remove_from_watchlater, name='remove_from_watchlater'),
    path('recorder', views.recorder_view, name='recorder'),
]

from django.urls import path
from . import views

urlpatterns = [
   path('',views.home,name='home'),
   path('register/',views.Register_user,name='register'),
   path('login/',views.login_user,name="login"),
   path('landingpage/',views.land,name="land"),
    path('logout/',views.logout_user,name="logout"),
    path('movielist/',views.movielist,name="movielist"),
    path('serieslist/',views.series_list,name="serieslist"),
     path('animelist/',views.anime_list,name="animelist"),
]
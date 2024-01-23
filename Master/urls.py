from django.urls import path
from . import views

app_name = "Master"

urlpatterns = [
   path('master/',views.master_page,name="admin_login"),
   path('admin_dashboard/',views.admin_login,name="admin_dashboard"),
   path('usermanagement/',views.usermanagement,name="usermanagement"),
   path('moviemanagement/',views.moviemanagement,name="moviemanagement"),
   path('moviedetails/<int:id>',views.movie_details,name="moviedetails"),
   path('addmovieform/',views.addmoviesform,name="addmoviesform"),
   path('editmovies/<int:id>',views.edit_movie,name="edit_movie"),
   path('deletemovie/<int:id>',views.delete_movie,name="deletemovie"),
]

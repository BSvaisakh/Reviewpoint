from django.urls import path
from . import views

app_name = "Master"

urlpatterns = [
   
   #####################ADMIN####################################
   
   path('master/',views.master_page,name="admin_login"),
   path('admin_dashboard/',views.admin_login,name="admin_dashboard"),
   
   ####################User#########################################
   
   path('usermanagement/',views.usermanagement,name="usermanagement"),
   path('adduser/',views.add_user,name="addUser"),
   # path('edituser/<int:id>',views.edit_user,name="editUser"),
   path('deleteuser/<int:id>',views.delete_user,name="deleteUser"),
   
   #####################Movies######################################
   
   path('moviemanagement/',views.moviemanagement,name="moviemanagement"),
   path('moviedetails/<int:id>',views.movie_details,name="moviedetails"),
   path('addmovieform/',views.addmoviesform,name="addmoviesform"),
   path('editmovies/<int:id>',views.edit_movie,name="editmovie"),
   path('deletemovie/<int:id>',views.delete_movie,name="deletemovie"),
   
   ######################series#####################################
   path('seriesmanagement/',views.seriesmanagement,name="seriesManagement"),
   path('seriesdetails/<int:id>',views.series_details,name="seriesdetails"),
   path('addseriesform/',views.addseriesform,name="addseriesform"),
   path('editseries/<int:id>',views.edit_series,name="editseries"),
    path('deleteseries/<int:id>',views.delete_series,name="deleteseries"),
    
    ################Animes###########################################
    path('animemanagement/',views.animemanagement,name="animeManagement"),
    path('animedetails/<int:id>',views.anime_details,name="animedetails"),
    path('addanimeform/',views.add_anime,name="addanimeform"),
    path('editanime/<int:id>',views.edit_anime,name="editanime"),
    path('deleteanime/<int:id>',views.delete_anime,name="deleteanime"),
    
    #################Movie Review################################
    
    path('MovieReview/<int:id>',views.add_Movie_Review,name="movieReview"),
    path('SeriesReview/<int:id>',views.add_series_Review,name="seriesReview"),
    path('AnimeReview/<int:id>',views.add_anime_Review,name="animeReview"),
    
    
    path('editMovieReview/<int:movie_id>/<int:review_id>',views.edit_movie_reviews,name="edit_movie_review"),
    path('deleteMovieReview/<int:movie_id>/<int:review_id>',views. delete_movie_reviews,name="delete_movie_review")
    
]

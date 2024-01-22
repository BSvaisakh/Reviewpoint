from django.urls import path
from . import views

urlpatterns = [
   path('master/',views.master_page,name="admin_login"),
   path('admin_dashboard/',views.admin_login,name="admin_dashboard"),
]

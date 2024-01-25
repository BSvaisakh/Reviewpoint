from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from .models import *
from .forms import *
# Create your views here.

###################ADMIN###########################

##############ADMIN LOGIN PAGE############

def master_page(request):
    request.session.clear()
    return render(request,"admin_login.html")

############# Admin DASHBOARD##############

def admin_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(password)

        user = User.objects.get(username=username)
        if user.is_superuser:
            if password == "0471":
                return render (request,"admin_dashboard.html")
            else :
                return redirect('admin_login')
        else :
            return redirect('home')
    return redirect('home')

####################USERS#########################

###########User Management#############
def usermanagement(request):
    users = User.objects.all()
    return render(request,"usermanage.html",{"users" : users})  

###################ADD USER#################
def add_user(request):
    if request.method == "POST":
        form = AddUserForm(request.POST) 
        
        if form.is_valid():
            user = form.save()
            user.save()
            return redirect('Master:usermanagement')
    else :
        form = AddUserForm()
        return render(request,"addform.html",{"form":form})  
    
# def edit_user(request,id):
#     user = User.objects.get(id=id)
#     if request.method == "POST":
#         form = AddUserForm(request.POST or None)
#         if form.is_valid():
#             data=form.save(commit=False)
#             data.save()
#             return redirect("Master:usermanagement",id)
#     else :
#         form = AddUserForm(instance=user)
#     return render(request,'addUser.html',{"form":form})
    
#################EDIT USER##############
def delete_user(request,id):
    if request.method == "GET":
        user = User.objects.get(id=id)
        user.delete()
        return redirect('Master:usermanagement')   
    return redirect('Master:usermanagement')  

############MOVIES##################################

###############MOVIE MANAGEMENT##############

def moviemanagement(request):
    
    allmovies = Movie.objects.all()
    context = {
        "movies" : allmovies
    } 
    return render(request,"shows.html",context)     

#################MOVIE DETAILS PAGE#################

def movie_details(request,id):
    user = User.objects.all()
    if user :
        username = request.session.get('username', None)
    movie = Movie.objects.get(id=id)
    context = {
        "movie" : movie,
        "data": username,
    }
    
    return render (request,"details.html",context)

#####################ADDING MOVIES###################
def addmoviesform(request):
    if request.method == "POST":
        form = Movieform(request.POST or None)
        if form.is_valid():
            data=form.save(commit=False)
            data.save()
            return redirect('Master:moviemanagement')
        print("form.errors")
    else :
        form =Movieform()
        return render(request,"addform.html",{"form": form})

####################EDIT MOVIES#####################

def edit_movie(request,id):
    movie = Movie.objects.get(id=id)
    if request.method == "POST" :
        form = Movieform(request.POST or None,instance=movie)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return redirect("Master:moviedetails",id)
    else :
        form = Movieform(instance=movie)
    return render(request,"addform.html",{"form":form})
    
###############DELETE MOVIES###################

def delete_movie(request,id):
    if request.method == "GET" :
        movie = Movie.objects.get(id=id)
        movie.delete()
        return redirect('Master:moviemanagement')
    
###################WEB SERIES#####################

#####################SERIES MANAGEMENT###################    

def seriesmanagement(request):
    
    allseries = Series.objects.all()
    context = {
        "series" : allseries
    } 
    return render(request,"shows.html",context)  

#############SERIES DETAILS PAGE#################

def series_details(request,id):
    user = User.objects.all()
    if user :
        username = request.session.get('username', None)
    series = Series.objects.get(id=id)
    context = {
        "series" : series,
        "data": username,
    }
    
    return render (request,"details.html",context)

#################SERIES ADDING PAGE######################

def addseriesform(request):
    if request.method == "POST":
        form = Seriesform(request.POST or None)
        if form.is_valid():
            data=form.save(commit=False)
            data.save()
            return redirect('Master:seriesManagement')
        print("form.errors")
    else :
        form =Seriesform()
        return render(request,"addform.html",{"form": form})
    
#####################SERIES EDITING###################
    
def edit_series(request,id):
    series = Series.objects.get(id=id)
    if request.method == "POST" :
        form = Seriesform(request.POST or None,instance=series)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return redirect("Master:seriesdetails",id)
    else :
        form = Seriesform(instance=series)
    return render(request,"addform.html",{"form":form})
    
###############DELETING SERIES###################

def delete_series(request,id):
    if request.method == "GET" :
        series = Series.objects.get(id=id)
        series.delete()
        return redirect('Master:seriesManagement')
    
###############################################################

#################Anime####################################

def animemanagement(request):
    
    allanime = Anime.objects.all()
    context = {
        "animes" : allanime
    } 
    return render(request,"shows.html",context)  

#############Anime DETAILS PAGE#################

def anime_details(request,id):
    user = User.objects.all()
    if user :
        username = request.session.get('username', None)
    anime = Anime.objects.get(id=id)
    context = {
        "animes" : anime,
        "data": username,
    }
    return render (request,"details.html",context)

######################Add anime##########################

def add_anime(request):
    if request.method == "POST":
        form = Animeform(request.POST or None)
        if form.is_valid():
            data=form.save(commit=False)
            data.save()
            return redirect('Master:animeManagement')
        print("form.errors")
    else :
        form =Animeform()
        return render(request,"addform.html",{"form": form})
    
####################Edit Anime########################

def edit_anime(request,id):
    anime = Anime.objects.get(id=id)
    if request.method=="POST":
        form = Animeform(request.POST or None ,instance=anime)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return redirect("Master:animedetails",id)
    else :
        form = Animeform(instance=anime)
        return render(request,"addform.html",{"form":form})
        
#################Delete Anime###############################

def delete_anime(request,id):
    if request.method =="GET":
        anime = Anime.objects.get(id=id)
        anime.delete()
        return redirect("Master:animeManagement")
        
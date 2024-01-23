from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from .models import *
from .forms import *
# Create your views here.

def master_page(request):
    request.session.clear()
    return render(request,"admin_login.html")
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

def usermanagement(request):
    users = User.objects.all()
    return render(request,"usermanage.html",{"users" : users})     

def moviemanagement(request):
    
    allmovies = Movie.objects.all()
    context = {
        "movies" : allmovies
    } 
    return render(request,"movies.html",context)     

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
        return render(request,"addmovies.html",{"form": form})

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
    return render(request,"addmovies.html",{"form":form})
    


def delete_movie(request,id):
    if request.method == "GET" :
        movie = Movie.objects.get(id=id)
        movie.delete()
        return redirect('Master:moviemanagement')
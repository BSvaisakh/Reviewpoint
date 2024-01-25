from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from Master.models import *
# from django.contrib.auth import authenticate,login,logout

# Create your views here.

##################HOME PAGE####################
def home(request):
    return render(request,"home.html")

#####################USER REGISTRATION###############

def Register_user(request):
    if request.method == "POST" :
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            user = User.objects.create(username=username,email=email,password=password)
            user.save()
            
            return redirect('home')
        else :
             response=f"""
            <script>
            window.alert("User already Exists")
            window.location.href='/';
            </script>
            """
             return HttpResponse(response)
    return redirect('home')

#######################USER LOGIN#######################

def login_user(request):
    if request.method == "GET":
        return render(request,"home.html")
    elif request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user=User.objects.filter(username=username).first()
        if user is not None:
            stored_password = user.password  # Assuming user.password contains the plain-text password
            if password == stored_password:
                request.session['username'] = username
                return render(request,"landing_page.html",{"data":username})
            else:
                response = f"""
                <script>
                window.alert('WRONG PASSWORD')
                window.location.href ='/';
                </script>
                """
                return HttpResponse(response)
        else:
            response = f"""
            <script>
            window.alert('No User Found')
            window.location.href ='/';
            </script>
            """
            return HttpResponse(response)

###################USER LOGOUT######################

def logout_user(request):
    request.session.clear()
    return redirect("/")

###################MOVIES LIST####################

def movielist(request):
    username = request.session.get('username', None)
    allmovies = Movie.objects.all()
    context = {
        "movies": allmovies,
        "data": username,
    } 
    return render(request,"shows.html",context)

#######################SERIES LIST####################

def series_list(request):
    username = request.session.get('username', None)
    allseries = Series.objects.all()
    context = {
        "series" : allseries,
        "data" : username,
    }
    return render(request,"shows.html",context)

def anime_list(request):
    username = request.session.get('username', None)
    allanime = Anime.objects.all()
    context = {
        "animes" : allanime,
        "data" : username,
    }
    return render(request,"shows.html",context)
    
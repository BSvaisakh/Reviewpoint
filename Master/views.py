from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
# Create your views here.

def master_page(request):
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
    return render(request,"movies.html")     
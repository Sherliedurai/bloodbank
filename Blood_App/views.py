from django.shortcuts import render,redirect
from forms import RegistrationForm,LoginForm

def registration(request):
    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            registered = form.save()

    return render(request,'registration.html',{'form':form})

def login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid() != "No User Found":
            return redirect("home")
        else:
            return redirect("login")

    return render(request, 'login.html', {'form': form})

def home(request):
    return render(request,'home.html')
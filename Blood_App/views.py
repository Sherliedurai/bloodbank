from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from forms import RegistrationForm, LoginForm, DonateForm
from django.contrib.auth import login, logout
from models import BloodPouch,Request,RegisteredUser


def donate_blood(request):
    Users = RegisteredUser.objects.all().filter(user=request.user)
    User = RegisteredUser()
    for user in Users:
        User = user
    if request.method == 'POST':
        form = DonateForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.address = User.address
            form.donated_by = User
            form.blood_type = User.blood_group
            form.save()
            return redirect('home')
    else:
        form = DonateForm()
        return render(request,'donate.html',{'form':form})


def registration(request):
    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            registered = form.save()
            return redirect('login')

    return render(request,'registration.html',{'form':form})

def userLogin(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid() != "No User Found":
            login(request,form.is_valid())
            return redirect("home")
        else:
            return redirect("login")

    return render(request, 'login.html', {'form': form})

@login_required()
def home(request):

    blood =  BloodPouch.objects.values('id','blood_type__group','quantity','chlorestrol_level','address__city','address__street').filter(is_requested=0)

    return render(request,'home.html',{'bloods':blood,'user':request.user})

@login_required()
def requestblood(request,pk):

    blood = get_object_or_404(BloodPouch,id=pk)

    blood.is_requested=1

    blood.save()

    user = request.user

    registered_user = RegisteredUser.objects.filter(user__email=user).last()

    Request.objects.create(requested_by=registered_user,requested_pouch=blood)

    return redirect('home')

def logout_view(request):
    logout(request)

    return redirect('login')

def blood_bank_admin(request):

    blood =  BloodPouch.objects.values('id','blood_type__group','quantity','chlorestrol_level','address__city','address__street').filter(is_requested=0)

    requested = Request.objects.values('id','requested_by__user__first_name','requested_by__contact','requested_pouch__blood_type__group').filter(is_issued=0)

    return render(request,'admin.html',{'bloods':blood,'requests':requested})

def issue_blood(request,pk):

    request = get_object_or_404(Request,id=pk)
    request.is_issued=1
    request.save()

    return redirect('admin')




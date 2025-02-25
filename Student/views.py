from django.shortcuts import render
from Student.forms import *
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def login_required(func):
    def inner(request,*args,**kwargs):
       un = request.session.get('username')
       if un:
           return func(request,*args,**kwargs)
       return HttpResponseRedirect(reverse('Student_login'))
    return inner

def Student_home(request):
    un = request.session.get('username')
    UO = User.objects.get(username=un)
    if UO:
        PO = StudentProfile.objects.get(username=UO)
        d = {'UO':UO,'PO':PO}
        # print(PO)
        return render(request,'student/Student_home.html',d)
    return render(request,"student/Student_home.html")

def Student_register(request):
    ESUFO = StudentUserForm()
    ESPFO = StudentProfileForm()
    d = {'ESUFO':ESUFO,'ESPFO':ESPFO}
    if request.method == 'POST' and request.FILES:
        SUFDO = StudentUserForm(request.POST)
        SPFDO = StudentProfileForm(request.POST,request.FILES)
        if SUFDO.is_valid() and SPFDO.is_valid():
            pw = SUFDO.cleaned_data.get('password')
            MSUFDO = SUFDO.save(commit=False)
            MSUFDO.set_password(pw)
            MSUFDO.save()
            MSPFDO = SPFDO.save(commit=False)
            MSPFDO.username = MSUFDO
            MSPFDO.save()
            return HttpResponseRedirect(reverse('Student_login'))
        return HttpResponse("Invalid Data!!!!")
    return render(request,"student/Student_register.html",d)

def Student_login(request):
    if request.method == 'POST':
        un = request.POST.get('un')
        pw = request.POST.get('pw')
        AUO = authenticate(username=un,password=pw)
        if AUO:
            login(request,AUO)
            request.session['username']=un
            return HttpResponseRedirect(reverse('Student_home'))
        return HttpResponse("Invalid Credentials!!!")
    return render(request,"student/Student_login.html")

@login_required
def Student_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('Student_home'))

@login_required
def my_ratings(request):
    un = request.session.get('username')
    SO = User.objects.get(username=un)
    d = {"SO":SO}
    # print(SO.ratings.all())  
    return render(request,"student/my_ratings.html",d)
    
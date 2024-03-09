from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect
from .models import Doctors,Pateint,Appointment

def Home(request):
    return render(request,'home.html')

def About(request):
    return render(request,'about.html')

def Contact(request):
    return render(request,'contact.html')

def Login(request):
    error=""
    if request.method=="POST":
        u=request.POST["uname"]
        p=request.POST["pwd"]
        user=authenticate(username=u,password=p)
        try:
            if user.is_staff:
                login(request,user)
                error="no"
            else:
                redirect ('admin_login')
                error="yes"
        except:
            error="yes"
    d={"error":error}
    return render(request,'login.html',d)

def Logout(request):
    if  not request.user.is_staff:
        redirect('admin_login')
    logout(request)
    return redirect('admin_login')

def Index(request):
    if not request.user.is_staff:
        return redirect('admin_login')
    doctor=Doctors.objects.all().count()
    pateint=Pateint.objects.all().count()
    apponmt=Appointment.objects.all().count()
    s={"d":doctor,"p":pateint,"a":apponmt}
    return render(request,"index.html",s)

def View_doctor(request):
    doctor=Doctors.objects.all()
    d={"d":doctor}
    return render(request,"view_doctor.html",d)

def Delete_doctor(request,pk):
    del_doc=Doctors.objects.all().filter(pk=pk)
    del_doc.delete()
    return redirect('view_doctor')

def Add_doctor(request):
    error=""
    if request.method=="POST":
        n=request.POST["name"]
        m=request.POST["mob"]
        s=request.POST["sp"]
        try:
            Doctors.objects.create(name=n,mobile=m,special=s)
            error="no"
        except:
            error="yes"
    d={"error":error}
    return render(request,"add_doctor.html",d)

def View_pateint(request):
    patient=Pateint.objects.all()
    p={"p":patient}
    return render(request,"view_pateint.html",p)

def Delete_pateint(request,pk):
    del_pat=Pateint.objects.all().filter(pk=pk)
    del_pat.delete()
    return redirect('view_pateint')

def Add_pateint(request):
    error=""
    if request.method=="POST":
        n=request.POST["name"]
        g=request.POST["gen"]
        m=request.POST["mob"]
        add=request.POST["address"]
        try:
            Pateint.objects.create(name=n,gender=g,mobile=m,address=add)
            error="no"
        except:
            error="yes"
    d={"error":error}
    return render(request,"add_pateint.html",d)

def View_appointment(request):
    appointment=Appointment.objects.all()
    a={"a":appointment}
    return render(request,"view_appointment.html",a)

def Delete_appointment(request,pk):
    del_apt=Appointment.objects.all().filter(pk=pk)
    del_apt.delete()
    return redirect('view_appointment')

def Add_appointment(request):
    error=""
    doctors=Doctors.objects.all()
    pateint=Pateint.objects.all()
    if request.method=="POST":
        doc=request.POST["doctor"]
        p=request.POST["pateint"]
        da=request.POST["date"]
        t=request.POST["time"]
        doctor1=Doctors.objects.filter(name=doc).first()
        patnt1=Pateint.objects.filter(name=p).first()
        try:
            Appointment.objects.create(doctor=doctor1,pateint=patnt1,date=da,time=t,)
            error="no"
        except:
            error="yes"
    d={"error":error,"doc":doctors,"patient":pateint}
    return render(request,"add_appointment.html",d)


          


# Create your views here.

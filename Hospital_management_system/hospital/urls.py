from django.contrib import admin
from django.urls import path
from .views import Home,About,Contact,Login,Logout,Index,View_doctor,View_pateint,View_appointment,Delete_doctor,Delete_pateint,Delete_appointment,Add_doctor,Add_pateint,Add_appointment

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home,name='home'),
    path('about/',About,name='about'),
    path('index/',Index,name='index'),
    path('contact/',Contact,name='contact'),
    path('login/',Login,name='admin_login'),
    path('logout/',Logout,name='admin_logout'),
    path('view_doctor/',View_doctor,name='view_doctor'),
    path('delete_doctor/<int:pk>/',Delete_doctor,name='delete_doctor'),
    path('add_doctor/',Add_doctor,name='add_doctor'),
    path('view_pateint/',View_pateint,name='view_pateint'),
    path('delete_pateint/<int:pk>/',Delete_pateint,name='delete_pateint'),
    path('add_pateint/',Add_pateint,name='add_pateint'),
    path('view_appointment/',View_appointment,name='view_appointment'),
    path('delete_appointment/<int:pk>/',Delete_appointment,name='delete_appointment'),
    path('add_appointment/',Add_appointment,name='add_appointment'),
]
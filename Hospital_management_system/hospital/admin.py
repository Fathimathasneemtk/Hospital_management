from django.contrib import admin
from .models import Pateint,Doctors,Appointment

admin.site.register(Doctors)
admin.site.register(Pateint)
class AppointmentAdmin(admin.ModelAdmin):
    list_display=('id','doctor','pateint','date','time')
admin.site.register(Appointment,AppointmentAdmin)


# Register your models here.

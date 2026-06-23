from django.contrib import admin
from . models import *
# Register your models here.
class ClinicAdminDT(admin.ModelAdmin):
    readonly_fields = ('date_time',)
    
class DepartmentDT(admin.ModelAdmin):
    readonly_fields = ('date_time',)
    
class DoctorDT(admin.ModelAdmin):
    readonly_fields = ('date_time',)
    
class NurseDT(admin.ModelAdmin):
    readonly_fields = ('date_time',)
    
class StaffDT(admin.ModelAdmin):
    readonly_fields = ('date_time',)
    
class PatientDT(admin.ModelAdmin):
    readonly_fields = ('date_time',)
    
admin.site.register(ClinicAdmin, ClinicAdminDT)
admin.site.register(Department, DepartmentDT)
admin.site.register(Doctor, DoctorDT)
admin.site.register(Patient, PatientDT)
admin.site.register(Nurse, NurseDT)
admin.site.register(Staff, StaffDT)


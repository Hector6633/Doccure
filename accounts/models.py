from django.db import models

# Create your models here.
class ClinicAdmin(models.Model):
     clinic_id = models.IntegerField(unique=True, primary_key=True)
     clinic_name = models.CharField(max_length=100)
     clinic_email = models.EmailField()
     status = models.CharField(default='Active')
     date_time = models.DateTimeField(auto_now_add=True)
     
     def __str__(self):
          return self.clinic_name
        
class Department(models.Model):
    department_id = models.IntegerField(unique=True, primary_key=True)
    department_name = models.CharField(max_length=100)
    department_email = models.EmailField()
    status = models.CharField(default='Active')
    date_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.department_name
      
class Doctor(models.Model):
    doctor_id = models.IntegerField(unique=True, primary_key=True)
    doctor_name = models.CharField(max_length=100)
    doctor_email = models.EmailField()
    doctor_mob_number = models.CharField(max_length=10)
    specialization = models.CharField(max_length=200, blank=True)
    license_number = models.CharField(max_length=100, blank=True)
    years_of_experience = models.IntegerField(null=True, blank=True)
    consultation_fee = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    clinic_id = models.ForeignKey(ClinicAdmin, on_delete=models.CASCADE)
    status = models.CharField(default='Active')
    date_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.doctor_name
    
class Nurse(models.Model):
    nurse_id = models.IntegerField(unique=True, primary_key=True)
    nurse_name = models.CharField(max_length=100)
    nurse_email = models.EmailField()
    nurse_mob_number = models.CharField(max_length=10)
    years_of_experience = models.IntegerField(null=True, blank=True)
    clinic_id = models.ForeignKey(ClinicAdmin, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    status = models.CharField(default='Active')
    date_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nurse_name
    
class Patient(models.Model):
    patient_id = models.IntegerField(unique=True, primary_key=True)
    patient_name = models.CharField(max_length=100)
    patient_email = models.EmailField()
    patient_mob_number = models.CharField(max_length=10)
    status = models.CharField(default='Active')
    date_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.patient_name
    
class Staff(models.Model):
    staff_id = models.IntegerField(unique=True, primary_key=True)
    staff_name = models.CharField(max_length=100)
    staff_email = models.EmailField()
    staff_mob_number = models.CharField(max_length=10)
    status = models.CharField(default='Active')
    date_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.staff_name
    
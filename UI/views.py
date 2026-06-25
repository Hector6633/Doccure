from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def doctor_dashboard(request):
    return render(request, 'doctor-dashboard.html')

def nurse_dashboard(request):
    return render(request, 'nurse-dashboard.html')

def patient_dashboard(request):
    return render(request, 'patient-dashboard.html')

def reception_dashboard(request):
    return render(request, 'reception-dashboard.html')

def terms_condition(request):
    return render(request, 'term-condition.html')

def privacy_policy(request):
    return render(request, 'privacy-policy.html')
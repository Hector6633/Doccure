from django.urls import path
from . views import *

urlpatterns = [
    path('', index, name='index'),
    path('doctor_dashboard/', doctor_dashboard, name='doctor_dashboard'),
    path('nurse_dashboard/', nurse_dashboard, name='nurse_dashboard'),
    path('reception_dashboard/', reception_dashboard, name='reception_dashboard'),
    path('patient_dashboard/', patient_dashboard, name='patient_dashboard'),
    path('terms_condition/', terms_condition, name='terms_condition'),
    path('privacy_policy/', privacy_policy, name='privacy_policy'),
]

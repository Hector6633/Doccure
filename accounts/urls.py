from django.urls import path
from . views import *

urlpatterns = [
    path('', index, name='index'),
    path('doctor_dashboard/', doctor_dashboard, name='doctor_dashboard'),
    path('register/', register, name='register'),
    path('login/', login_, name='login'),
    path('logout/', logout_, name='logout'),
]

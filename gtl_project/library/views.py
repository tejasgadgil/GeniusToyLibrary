from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'library/home.html')

def about_us(request):
    return render(request,'library/aboutUs.html')

def contact_us(request):
    return render(request,'library/contactUs.html')

def membership_plans(request):
    return render(request,'library/membershipPlans.html')

def t_and_c(request):
    return render(request,'library/termsAndConditions.html')



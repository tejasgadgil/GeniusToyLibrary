from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="gtl-home"),
    path('about/',views.about_us,name="gtl-aboutUs"),
    path('contact/',views.contact_us,name="gtl-contactUs"),
    path('membership-plans/',views.membership_plans,name="gtl-membershipPlans"),
    path('terms-&-conditions/',views.t_and_c,name="gtl-t&c")
]
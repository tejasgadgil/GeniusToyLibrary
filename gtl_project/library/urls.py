from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="gtl-home"),
    path('about/',views.about_us,name="gtl-aboutUs"),
]
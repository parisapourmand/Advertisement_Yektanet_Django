from django.urls import path
from . import views


app_name = 'advertiser_management'
urlpatterns = [
    path('', views.HomeView.as_view(), name='advertiserManagement-home'),
]
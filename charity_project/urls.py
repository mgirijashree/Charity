from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('causes/', views.causes, name='causes'),
    path('donate/', views.donate, name='donate'),
    path('donate-success/', views.donate_success, name='donate_success'),
    path('contact/', views.contact, name='contact'),
    path('volunteer/', views.volunteer, name='volunteer'),
    path("subscribe-email/",views.subscribe_email,name="subscribe_email"),

]
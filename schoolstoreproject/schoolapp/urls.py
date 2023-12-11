from django.urls import path
from . import views

app_name = 'schoolapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('new_page/', views.new_page, name='new_page'),
    path('department/', views.department, name='department'),
    path('logout/', views.logout, name='logout'),
]

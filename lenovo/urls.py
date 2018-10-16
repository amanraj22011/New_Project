from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'lenovo'

urlpatterns = [
    path('',views.Home, name =  'home'),
    
    path('<int:val>/', views.detail, name = 'detail'),

    path('add/', views.add_new, name = 'login'),
    
    path('login/', views.login_form, name = 'Login'),

    path('logout/', views.logout_form, name = 'logout'),
]
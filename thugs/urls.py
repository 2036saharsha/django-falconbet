from django.urls import path
from . import views
urlpatterns = [
    path('', views.hi, name='HOME'),
    path('register', views.register, name='register'),
    path('data', views.data, name='data'),
    path('login',views.login, name='login'),
    path('logout',views.logout, name='logout'),
    path('table',views.table, name='table'),
]

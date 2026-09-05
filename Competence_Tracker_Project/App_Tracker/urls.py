from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name= "home"),
    path('participant/', views.participant, name='participants'),
    path('content_list/', views.content_list, name='content_list'),
    path('task_list/', views.task_list, name='task_list'),
    path('admin_dashboard/',views.admin_dashboard, name='admin_dashboard'),
    path('logout/', views.logout, name='logout'),
    path('login/', views.login , name='login'),
    path('register/', views.register, name='register'),
    path('pending_approval', views.pending_approval, name='pending_approval'),
    path('task_form', views.task_form, name='task_form')
]

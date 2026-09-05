from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
# Create your views here.

def home_page(request):
    return render(request, "base.html")

def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    return render(request, 'accounts/login.html')

def admin_dashboard(rqeuest):
    return render(request, 'dashboard/admin_dashboard.html' )

def participant(request):
    return render(request, 'dashboard/participant_dashboard.html')

def content_list(reqeust):
    return render(request, 'learning/content_list.html')

def task_list(request):
    return render(requst, 'tasks/task_list')

def register(request):
    return render(request, 'accounts/register.html')

def pending_approval(request):
    return render(request, 'accounts/pending_approval.html')

def task_form(request):
    return render(request, 'tasks/task_form.html')
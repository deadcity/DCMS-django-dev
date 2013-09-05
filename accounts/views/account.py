from django.shortcuts import render
from django.views import generic

def register(request):
    return render(request, 'accounts/register.html')

from django.shortcuts import render
from django.shortcuts import redirect
from django.views import generic
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from django.shortcuts import render_to_response

def register(request):
		if request.POST:
				user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
				user.last_name = request.POST['last_name']
				user.first_name = request.POST['first_name']
				user.save()
				redirect('login', message="Your account has been created. You can now log in below.")
				return
		return render(request, 'accounts/register.html')

def profile(request):
	return render(request, 'accounts/profile.html')
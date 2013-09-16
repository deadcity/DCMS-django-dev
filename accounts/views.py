from django.shortcuts import render
from django.shortcuts import redirect
from django.views import generic
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import re

def register(request):
		if request.POST:
				if request.POST['username'].strip() != "" and re.match(r"[^@]+@[^@]+\.[^@]+", request.POST['email']) and request.POST['password'] != "":
					user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
					user.last_name = request.POST['last_name']
					user.first_name = request.POST['first_name']
					user.save()
					messages.success(request, 'Your account was created. You can log in below.')
					return redirect('login')
				else:
					messages.error(request, 'There was an error creating your account.')
					return redirect('register')
		return render(request, 'accounts/register.html')

@login_required
def profile(request):
	return render(request, 'accounts/profile.html')
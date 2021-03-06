from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from portal.forms import RegistrationForm, AccountAuthenticationForm 
from .models import Job, Profile


def registration_view(request):
	context = {}
	if request.POST:
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			email = form.cleaned_data.get('email')
			raw_password = form.cleaned_data.get('password1')
			account = authenticate(email=email, password=raw_password)
			login(request, account)
			return redirect('home')
		else:
			context['registration_form'] = form

	else:
		form = RegistrationForm()
		context['registration_form'] = form
	return render(request, 'portal/register.html', context)


def logout_view(request):
	logout(request)
	return redirect('home')



def login_view(request):

	context = {}

	user = request.user
	if user.is_authenticated: 
		return redirect("home")

	if request.POST:
		form = AccountAuthenticationForm(request.POST)
		if form.is_valid():
			email = request.POST['email']
			password = request.POST['password']
			user = authenticate(email=email, password=password)

			if user:
				login(request, user)
				return redirect("home")

	else:
		form = AccountAuthenticationForm()

	context['login_form'] = form

	# print(form)
	return render(request, "portal/login.html", context)


def home(request):
    jobs = Job.objects.all()
    profile = Profile.objects.all()
    context = {'jobs':jobs, 'profile':profile}

    return render(request, 'portal/landing.html', context)

def profile(request):
    profile = Profile.objects.all()
    context = {'profile': profile}
    return render(request, 'portal/profile.html', context)


def joblist(request, pk_test ):
    job = Job.objects.get(id=pk_test)
    context = {'job': job}
    return render(request, 'portal/joblist.html', context)



# def jobdetailview(request, pk):
#     job = Jobs.objects.get(id=pk)
#     context = {'job': job}
#     return render(request, 'portal/jobslist.html')
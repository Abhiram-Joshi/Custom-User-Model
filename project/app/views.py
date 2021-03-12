from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse
from .forms import SignupForm

# Create your views here.
def home(request):
    return render(request, 'home.html')



def user_login(request):

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(username = email, password = password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))

            else:
                return HttpResponse("Account not active!!")

        else:
            return HttpResponse("User not found!")

    else:
        return render(request, 'login.html')


def signup(request):
    registered = False

    if request.method=='POST':
        form = SignupForm(request.POST)

        if form.is_valid():

            user = form.save()
            user.set_password(user.password)
            user.save()

            registered = True

        else:
            print(form.errors)


    else:
        form = SignupForm()

    context_dict = {
        'registered':registered,
        'form':form,
    }

    return render(request, 'signup.html', context_dict)


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

@login_required
def user_info(request):
    return render(request, 'user_info.html', context={'email':request.user.email, 'phone':request.user.phone})

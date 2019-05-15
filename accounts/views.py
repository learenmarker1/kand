from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return HttpResponseRedirect(reverse('testapp:teacherview'))
            return HttpResponseRedirect(reverse('testapp:index'))
        else:
            messages.error(request, 'Fel användarnamn och/eller lösenord')

    return render(request, 'accounts/login.html', {})

def logout_user(request):
    logout(request)
    return render (request, 'accounts/login.html', {})

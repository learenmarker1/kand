from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    #return HttpResponse('<h1>We are the Mood managers</h1>')
    return render(request, 'testapp/home.html')

def about(request):
    #return HttpResponse('<h1>More about our mood managers</h1>')
    return render(request, 'testapp/about.html')

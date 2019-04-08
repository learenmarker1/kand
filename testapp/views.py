from django.shortcuts import render
#from django.http import HttpResponse
questions = [
    {
        'question': 'Hur många timmar sov du i natt?',
        'answer1': '6 timmar',
        'answer2': '7 timmar',
        'answer3': '8 timmar',
        'answer4': '9 timmar',
    },
    {
        'question': 'Kände du dig stressad över skolarbetet idag?',
        'answer1': 'Ja, väldigt',
        'answer2': 'Ganska mycket',
        'answer3': 'Ganska lite',
        'answer4': 'Inte alls',
    }
]

def home(request):
    #return HttpResponse('<h1>We are the Mood managers</h1>')
    context = {
        'questions': questions
    }
    return render(request, 'testapp/home.html', context)

def about(request):
    #return HttpResponse('<h1>More about our mood managers</h1>')
    return render(request, 'testapp/about.html')

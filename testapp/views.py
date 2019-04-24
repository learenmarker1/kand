from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'testapp/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'testapp/detail.html'


class DetailView1(generic.DetailView):
    model = Question
    template_name = 'testapp/question1.html'

class DetailView2(generic.DetailView):
    model = Question
    template_name = 'testapp/question2.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'testapp/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'testapp/detail.html',{
        'question': question,
        'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
    return HttpResponseRedirect(reverse('testapp:results', args=(question.id,)))


def answer1(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'testapp/question1.html',{
        'question': question,
        'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
    next_question_ids = Question.objects.filter(id__gt=question_id).order_by('id').values('id')
    if next_question_ids:
        next_question_id = next_question_ids[0]['id']
        return HttpResponseRedirect(reverse('testapp:question1', args=(next_question_id,)))
    else:
        HttpResponseRedirect(reverse('testapp:result'))

def answer2(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'testapp/detail.html',{
        'question': question,
        'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
    next_question_ids = Question.objects.filter(id__gt=question_id).order_by('id').values('id')
    if next_question_ids:
        next_question_id = next_question_ids[0]['id']
        return HttpResponseRedirect(reverse('testapp:question2', args=(next_question_id,)))
    else:
        return HttpResponseRedirect(reverse('testapp:result'))

def answer3(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'testapp/detail.html',{
        'question': question,
        'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
    next_question_ids = Question.objects.filter(id__gt=question_id).order_by('id').values('id')
    if next_question_ids:
        next_question_id = next_question_ids[0]['id']
        return HttpResponseRedirect(reverse('testapp:result', args=(next_question_id,)))
    else:
        return HttpResponseRedirect(reverse('testapp:result'))

def result(request):
    questions = Question.objects.all()
    # results = Question.get_result_dict()
    return render(request, 'testapp/result.html', {'questions': questions})

from django.conf import settings
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.template import loader
from django.utils import timezone
import random
from .forms import PostForm
from .models import Choice, Question, Poll, Post


class IndexView(generic.ListView):
    template_name = 'testapp/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self, **kwargs):
        """Return 3 random questions from the database."""
        return Poll.objects.latest('pk').questions.all()


class DetailView(generic.DetailView):
    model = Question
    template_name = 'testapp/detail.html'

class DetailView1(generic.DetailView):
    model = Question
    template_name = 'testapp/question1.html'

class DetailView2(generic.DetailView):
    model = Question
    template_name = 'testapp/question2.html'

class DetailView3(generic.DetailView):
    model = Question
    template_name = 'testapp/question3.html'


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


def result(request):
    questions = Poll.objects.latest('pk').questions.all()
    qresults = []
    for question in questions:
        qresults.append({'result':question.get_result_dict(),'question':question})
    return render(request, 'testapp/result.html', {'qresults' : qresults})


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
    next_question_ids = Poll.objects.latest('pk').questions.filter(id__gt=question_id).order_by('id').values('id')
    if next_question_ids:
        next_question_id = next_question_ids[0]['id']
        return HttpResponseRedirect(reverse('testapp:question2', args=(next_question_id,)))
    else:
        return HttpResponseRedirect(reverse('testapp:result'))

def answer2(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'testapp/question2.htlm',{
        'question': question,
        'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
    next_question_ids = Poll.objects.latest('pk').questions.filter(id__gt=question_id).order_by('id').values('id')
    if next_question_ids:
        next_question_id = next_question_ids[0]['id']
        return HttpResponseRedirect(reverse('testapp:question3', args=(next_question_id,)))
    else:
        return HttpResponseRedirect(reverse('testapp:result'))

def answer3(request, question_id ):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'testapp/question3.html',{
        'question': question,
        'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
    next_question_ids = Poll.objects.latest('pk').questions.filter(id__gt=question_id).order_by('id').values('id')
    if next_question_ids:
        next_question_id = next_question_ids[0]['id']
        return HttpResponseRedirect(reverse('accounts:login', args=(next_question_id,)))
    else:
        return HttpResponseRedirect(reverse('accounts:login'))

def teacherview(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('testapp/teacherview.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'testapp/post_list.html', {'posts':posts})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('testapp:post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'testapp/post_edit.html', {'form': form})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'testapp/post_detail.html', {'post': post})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('testapp:post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'testapp/post_edit.html', {'form': form})

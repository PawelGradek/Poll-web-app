from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Question, Choice


def index(request):
    ques_list = Question.objects.order_by('-pub_date')[:5]
    context = {'question_list': ques_list}
    return render(request, 'pollapp/index.html', context)

def choice(request, question_id):
    try:
        ques = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question not exist")
    return render(request, 'pollapp/choice.html', {'question': ques})


def score(request, question_id):
    ques = get_object_or_404(Question, pk=question_id)
    return render(request, 'pollapp/score.html', {'question': ques})


def user_vote(request, question_id):

    ques = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = ques.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):

        return render(request, 'pollapp/detail.html', {
            'question': ques,
            'error_message': "Didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('pollapp:score', args=(ques.id,)))

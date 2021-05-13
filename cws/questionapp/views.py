from django.shortcuts import render
from django.views.generic import ListView
from questionapp.models import Question
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.response import Response
from questionapp.serializers import QuestionSerializer
from django.http import HttpResponse, JsonResponse
import json

from questionapp.models import Answer, QuestionCard
from mainapp.models import Topic


def question_page(request, id):
    template = 'questionapp/question.html'
    context = {}
    context['topic_id'] = id
    context['topic'] = Topic.objects.get(pk=id).topic
    request.session['score'] = 0
    request.session['count'] = 0
    return render(request, template, context)


class TestListView(ListView):
    model = QuestionCard
    template_name = 'questionapp/testlist.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = QuestionCard.objects.all()
        return context


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get_queryset(self):
        id = self.kwargs["id"]

        if id != '0':
            queryset = Question.objects.filter(topic_id=id)
            return queryset

        queryset = Question.objects.all()
        return queryset


class QuestionPaginator(PageNumberPagination):
    page_size = 1


def answer(request):
    if request.method == "POST":
        
        message = json.loads(request.body)
        answers_on_question = [i['id'] for i in Answer.objects.values('id').filter(
            question_id=message['question_id'])]

        set_answers_on_question = set(answers_on_question)
        set_user_answers = set([int(item) for item in message['answers']])

        if not (set_user_answers.issubset(set_answers_on_question)):
            return HttpResponse(status=400)
        
        request.session['count'] = request.session.get('count') + 1
        true_answers = [i['id'] for i in Answer.objects.values('id').filter(
            question_id=message['question_id'], correct=True)]

        set_true_answers = set(true_answers)

        correct_answers, miss_answers, uncorrect_answers = [], [], []

        if set_true_answers == set_user_answers:
            correct_answers = message['answers']
            data = pack_data(correct_answers, miss_answers, uncorrect_answers)
            request.session['score'] = request.session.get('score') + 1
            return JsonResponse(data)

        else:
            correct_answers = list(set_user_answers & set_true_answers)
            uncorrect_answers = list(set_user_answers - set_true_answers)
            miss_answers = list(set_true_answers - set_user_answers)
            data = pack_data(correct_answers, miss_answers, uncorrect_answers)
            return JsonResponse(data)
       
    if request.method == "GET":
        data = {
            'score': request.session.get('score'),
            'count': request.session.get('count')
        }
        return JsonResponse(data)
    


def pack_data(correct_answers, miss_answers, uncorrect_answers):
    data = {
        'correct_answers': correct_answers,
        'uncorrect_answers': uncorrect_answers,
        'miss_answers': miss_answers
    }
    return data

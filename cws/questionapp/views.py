from django.shortcuts import render
from django.views.generic import ListView
from questionapp.models import Question
from rest_framework import viewsets 
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics

from questionapp.serializers import QuestionSerializer


def question_page(request):
    template = 'questionapp/question.html'
    return render(request, template)


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class =  QuestionSerializer
    template = 'questionapp/question.html'
    def get_queryset(self):
        search = self.request.GET.get('search')
        queryset = super().get_queryset()
        if search:
            queryset = queryset.filter(name__icontains=search)
        return queryset


class QuestionPaginator(PageNumberPagination):
     page_size = 1



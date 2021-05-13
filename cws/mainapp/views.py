from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, PageNotAnInteger
from django.views.generic import ListView
from mainapp.serializers import ContentCardSerializer, CommentSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from mainapp.models import Card, ContentCard, Topic, Comment
from django.contrib.auth.decorators import login_required




class Home(ListView):
    model = Card
    template_name = 'mainapp/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = Card.objects.all().order_by('order')
        return context


class EducationListView(ListView):
    model = ContentCard
    template_name = 'mainapp/education.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        id = context['view'].kwargs["id"]
        context['object_list'] = ContentCard.objects.filter(
            topic_id=id).order_by('order')
        context['comment_list'] = Comment.objects.filter(topic_id=id)
        context['title'] = Topic.objects.get(pk=id).topic
        context['topic_id'] = id
        paginator = Paginator(context['object_list'], 1)
        education_card_number = self.request.GET.get('page', 1)
        context['object_list'] = paginator.get_page(education_card_number)
        return context


class ContentCardViewSet(viewsets.ModelViewSet):
    queryset = ContentCard.objects.all()
    serializer_class = ContentCardSerializer

    def get_queryset(self):
        search = self.request.GET.get('search')
        queryset = super().get_queryset()
        if search:
            queryset = queryset.filter(name__icontains=search)
        return queryset

from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, PageNotAnInteger
from django.views.generic import ListView
from mainapp.serializers import CardSerializer
from rest_framework import viewsets

from mainapp.models import Card, ContentCard, Topic


#def home(request):
#    card_list = Card.objects.all()
#   context = {'card_list' : card_list}
#    return render(request, 'mainapp/index.html', context)

class Home(ListView):
    model = Card
    template_name = 'mainapp/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = Card.objects.all().order_by('order')
        return context
    

def education(request, id):

    education_card_list = ContentCard.objects.filter(topic_id=id)
    paginator = Paginator(education_card_list, 1)
    education_card_number = request.GET.get('page', 1)
    education_card_obj = paginator.get_page(education_card_number)
    a = education_card_obj[0]
    return render(request, 'mainapp/education.html', 
                            {'object_list' : education_card_obj, 
                            'title' : education_card_obj[0].topic}) # take the topic_id field of the  1st element 


class EducationListView(ListView):
    model = ContentCard
    template_name='mainapp/education.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        id = context['view'].kwargs["id"]
        context['object_list'] = ContentCard.objects.filter(topic_id=id).order_by('order')
        context['title'] = Topic.objects.get(pk=id).topic
        paginator = Paginator(context['object_list'], 1)
        education_card_number = self.request.GET.get('page', 1)
        context['object_list'] = paginator.get_page(education_card_number)
        return context

class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    def get_queryset(self):
        search = self.request.GET.get('search')
        queryset = super().get_queryset()
        if search:
            queryset = queryset.filter(name__icontains=search)
        return queryset



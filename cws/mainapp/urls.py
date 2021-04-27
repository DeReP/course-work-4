from django.urls import path

from mainapp.views import CardViewSet

app_name = 'mainapp'

urlpatterns = [
     path('', Home.as_view(), name="Home")
]
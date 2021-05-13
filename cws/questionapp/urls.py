
from django.contrib import admin
from django.urls import path
from questionapp.views import answer

urlpatterns = [
    path('answer/', answer, name="answer_to_question")
]

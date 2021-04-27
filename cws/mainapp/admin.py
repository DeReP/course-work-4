from django.contrib import admin
from mainapp.models import Card, ContentCard, Topic
from questionapp.models import Question, Answer

@admin.register(Card)
class Card_Admin(admin.ModelAdmin):
    pass


@admin.register(ContentCard)
class Content_Card_Admin(admin.ModelAdmin):
    pass

@admin.register(Topic)
class Topic_Admin(admin.ModelAdmin):
    pass

@admin.register(Question)
class Question_Admin(admin.ModelAdmin):
    pass

@admin.register(Answer)
class Answer_Admin(admin.ModelAdmin):
    pass


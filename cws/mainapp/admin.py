from django.contrib import admin
from mainapp.models import Card, ContentCard, Topic, Comment
from questionapp.models import Question, Answer, QuestionCard

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


@admin.register(Comment)
class Comment_Admin(admin.ModelAdmin):
    pass


@admin.register(QuestionCard)
class Question_Card(admin.ModelAdmin):
    pass


from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from easy_thumbnails.fields import ThumbnailerImageField

from mainapp.models import Topic

class Question(models.Model):
    text = RichTextUploadingField(verbose_name='Содержание вопроса')
    topic = models.ForeignKey(
        "mainapp.Topic", verbose_name="Тема", on_delete=models.PROTECT, default=1)
    def get_answers(self):
        answers = Answer.objects.filter(question=self)
        return answers

    def __str__(self):
        return "{} | {}".format(self.topic, self.text)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name="относится к вопросу")
    text = models.CharField(max_length=512, verbose_name="Текст ответа")
    correct = models.BooleanField(verbose_name="Ответ верен?", default=False)

    def __str__(self):
        return "{} || {}".format(self.question, self.text)


class QuestionCard(models.Model):
    topic = models.ForeignKey(
        "mainapp.Topic", verbose_name="Тема теста", on_delete=models.PROTECT)
    text = models.CharField(max_length=512, verbose_name="Текст карточки")
    image = ThumbnailerImageField(
        upload_to='card_img/', verbose_name="Картинка карточки", blank=True, null=True)

    def __str__(self):
        return '{} | {}'.format(self.topic, self.text)

    def get_absolute_url(self):
        return reverse("question_page", args=[self.topic_id])

    def get_preview(self):
        if self.image:
            return self.image['preview'].url
        else:
            return ''






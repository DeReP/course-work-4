from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Question(models.Model):
    text = RichTextUploadingField(verbose_name='Содержание вопроса')

    def get_answers(self):
        answers = Answer.objects.filter(question=self)
        return answers


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name="относится к вопросу")
    text = models.CharField(max_length=512, verbose_name="Текст вопроса")
    correct = models.BooleanField(verbose_name="Ответ верен?", default=False)



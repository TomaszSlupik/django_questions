from django.db import models

# Create your models here.
class Question (models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(verbose_name="data published")

    def __str__(self) -> str:
        return f"Pytanie: {self.question_text}"



class Choice (models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.PositiveIntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')


    def __str__(self) -> str:
        return self.choice_text
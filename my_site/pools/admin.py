from django.contrib import admin
from pools.models import Question, Choice

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    fields = ["question_text", "pub_date"]
    list_display = ["question_text", "pub_date"]


class ChoiceAdmin(admin.ModelAdmin):
    fields = ["choice_text", "votes", "question"]
    list_display = ["choice_text", "votes", "question"]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
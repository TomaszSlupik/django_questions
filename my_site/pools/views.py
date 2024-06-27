from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from pools.models import Question, Choice
from django.views import generic

# Create your views here.
def index(request):
    questions = Question.objects.all()
    # question_txt =[q.question_text for q in questions]
    # content = "<br>".join(question_txt)
    # return HttpResponse (f"{content}")
    context = {"pytania": questions}
    return render(request, "index.html", context)

# Alternatywa dla wyświetlenia template Index
class QuestionListView(generic.ListView):
     template_name = "index.html"
     queryset = Question.objects.all()
     context_object_name = "pytania"

def bye (request):
    return render (request, "bye.html")

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'detail.html', {'question': question})

# Alternatywa dla wyświetlenia template details
class QuestionDetailView(generic.DetailView):
    template_name = "detail.html"
    model = Question
    context_object_name = "question"

# Alternatywa dla wyświetlenia template Result
class QuestionResultView(QuestionDetailView):
     template_name = "result.html"

def result(request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        return render(request, 'result.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        choice_id = request.POST["choice"]
        selected_choice = question.choices.get(pk=choice_id)
    except (KeyError, Choice.DoesNotExist):
        # Renderujemy stronę szczegółów pytania z komunikatem błędu, jeśli nie wybrano wyboru
        return render(request, "detail.html", {"question": question, "error_message": "You didn't select a choice."})
    else:
        # Inkrementujemy liczbę głosów dla wybranego wyboru i przekierowujemy na stronę wyników
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("result", args=(question.id,)))
    

# Alternatywa dla wyświetlenia template Choice
class ChoiceListView(generic.ListView):
    template_name = "choice.html"
    queryset = Choice.objects.all()
    context_object_name = "odpowiedzi"

    
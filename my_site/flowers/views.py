from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from flowers.models import Flowers


# Create your views here.
class FlowersListView(generic.ListView):
    template_name = 'flowers.html'
    queryset = Flowers.objects.all()
    context_object_name = "kwiaty"


def add_flower(request):
    if request.method == "POST":
        name_flower = request.POST.get("text")
        if name_flower:
            Flowers.objects.create(name_flower=name_flower)
            return redirect('flowers') 
    kwiaty = Flowers.objects.all()
    return render(request, 'add_flower.html', {'kwiaty': kwiaty})


def edit_flower(request, flower_id):
    flower = get_object_or_404(Flowers, pk=flower_id)
    if request.method == "POST":
        name_flower = request.POST.get("text")
        if name_flower:
            flower.name_flower = name_flower
            flower.save()
            return redirect('flowers')  # Do listy kwiatów przekierowanie
    return render(request, 'edit_flower.html', {'flower': flower})


def delete_flower(request, flower_id):
    flower = get_object_or_404(Flowers, pk=flower_id)
    if request.method == "POST":
        flower.delete()
        return redirect('flowers')  # Do listy kwiatów przekierowanie
    return render(request, 'delete_flower.html', {'flower': flower})
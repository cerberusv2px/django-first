from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item


# Create your views here.

def index(response, id):
    # value = "nice" if id == 69 else str(id)
    ls = ToDoList.objects.get(id=id)
    # items = ls.item_set.get(id=id)
    # return HttpResponse("<h3>%s</h3><br><p>%s</p></br>" % (ls.name, str(items.text)))
    return render(response, 'main/list.html', {"ls": ls})


def home(response):
    # return HttpResponse("<h2>view 1</h2>")
    return render(response, 'main/home.html', {})

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList


# Create your views here.

def index(response, id):
    # value = "nice" if id == 69 else str(id)
    ls = ToDoList.objects.get(id=id)
    # items = ls.item_set.get(id=id)
    # return HttpResponse("<h3>%s</h3><br><p>%s</p></br>" % (ls.name, str(items.text)))
    return render(response, 'main/list.html', {"ls": ls})


def home(response):
    # return HttpResponse("<h2>view 1</h2>")
    todos = ToDoList.objects.all()
    return render(response, 'main/home.html', {"todos": todos})


def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()

        return HttpResponseRedirect("/%i" % t.id)
    else:
        form = CreateNewList()
    return render(response, "main/create.html", {"form": form})

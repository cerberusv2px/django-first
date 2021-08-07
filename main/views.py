from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(response):
    return HttpResponse("<h3>fuck this shit</h3>")


def v1(response):
    return HttpResponse("<h2>view 1</h2>")

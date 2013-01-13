from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from info.models import Document

def rules(request, type='rules', template="info/rules.html"):
    return render(request, template)

def bonus(request, type='bonus', template="info/bonus.html"):
    return render(request, template)

def regular(request, template="info/regular.html"):
    return render(request, template)

def index(request, template="info/index.html"):
    return render(request, template)

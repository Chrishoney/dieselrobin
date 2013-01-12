from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from info.models import Document

def rules(request, type='rules', template="info/rules.html"):
    rules = get_object_or_404(Document, type=type)
    return render(request, template, {'rules': rules})

def bonus(request, type='bonus', template="info/bonus.html"):
    bonus = get_object_or_404(Document, type=type)
    return render(request, template, {'bonus': bonus})

def regular(request, template="info/regular.html"):
    return render(request, template)

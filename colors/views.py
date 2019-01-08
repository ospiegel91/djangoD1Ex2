# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from .models import Colors

def index(request):
    return HttpResponse("Welcome to the Colors App")


def addColor(request, color_name):
    try:
        new_color = Colors(color_name=color_name)
        new_color.save()
        return HttpResponse("201 SUCCESS: {} created successfully".format(color_name))
    except:
        return HttpResponse("fucking error")


def getColor(request, color_name):
    try:
        color = Colors.objects.get(color_name=color_name)

        context = {
            'name': color
        }
        return render(request, 'colors/colorDetail.html', context)
    except:
        return HttpResponse("color does not exist, error:404")

def colorsList(request):
    color_list = Colors.objects.all();
    context ={
        'colors': color_list
    }

    return render(request, 'colors/index.html', context)

"""Perexmapp views"""

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# ...


def index(request):
    """PH"""
    return HttpResponse('I believe I can fly!')

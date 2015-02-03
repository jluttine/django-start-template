""" Base views for the project """

from django.shortcuts import render

def home(request):
    """ Default view for the root """
    return render(request, 'base.html')

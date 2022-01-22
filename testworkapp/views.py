from django.shortcuts import render

def index(request):
    return render(request, 'testworkapp/main.html')

def addnews(request):
    return render(request, 'testworkapp/addnews.html')


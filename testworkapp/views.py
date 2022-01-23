import datetime

from django.shortcuts import render,redirect
from .models import NewsList
from .forms import NewsListForm


def index(request):
    view = NewsList.objects.all()
    return render(request, 'testworkapp/main.html')

def addnews(request):
    error = ''
    if request.method == 'POST':
        form = NewsListForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect ('home')
        else: error = 'Ошибка!'
    form = NewsListForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'testworkapp/addnews.html',context)


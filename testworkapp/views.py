import datetime
from django.core.paginator import Paginator
from django.shortcuts import render,redirect
from django.http import HttpResponseNotFound, HttpResponseRedirect
from .models import NewsList, comment, backsaids
from .forms import NewsListForm, addComm, addSaid


def index(request):
    news = NewsList.objects.order_by('-views')[:5]
    context = {
        'news': news,
    }
    return render(request, 'testworkapp/main.html',context)

def allnews (request):
    news = NewsList.objects.order_by('date')
    paginator = Paginator(news, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'range': range(1, page_obj.paginator.num_pages+1)
    }
    return render(request, 'testworkapp/allnews.html', context)

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

def edit(request,id):
    try:
        view = NewsList.objects.get(id=id)
        if request.method == "POST":
            view.desc = request.POST.get('desc')
            view.save()
            return redirect('home')
        else:
            return render(request, "testworkapp/edit.html", {"view": view})
    except view.DoesNotExist:
        return HttpResponseNotFound('<h2>Data not found</h2>')

def shownews(request,id):
    error = ''
    news = NewsList.objects.get(id=id)
    news.views +=1
    news.save()
    comments = comment.objects.filter(nameArticle_id=id)

    if request.method == 'POST':
        addcomform = addComm(request.POST)
        if addcomform.is_valid():
            addc = comment.objects.create(nameArticle_id=id , Text = request.POST.get('Text'))
            return redirect('home')
        else: error = 'err'
    addcomform = addComm()
    context = {
        'news': news,
        'comments': comments,
        'formaddcom': addcomform,
        'error': error
    }
    return render(request, 'testworkapp/shownews.html', context)


def about(request):
    context = {

    }
    return render(request, 'testworkapp/about.html', context)


def backsaid(request):
    error = ''
    if request.method == 'POST':
        addSaids = addSaid(request.POST)
        if addSaids.is_valid():
            addSaids.save(commit=False)
            addSaids.save()
        else: error = 'UPS'
    addSaids = addSaid()
    context = {
        "addSaids": addSaids,
        "error": error
    }
    return render(request, 'testworkapp/backsaid.html', context)
from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {}
    context["articles"] = articles
    return render(request, "articles/index.html", context=context)

def create(request):
    return render(request, "articles/create.html")

def create_proc(request):
    title = request.POST.get("title")
    content = request.POST.get("content")
    Article.objects.create(title=title, content=content)
    return redirect("/")

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {}
    context["article"] = article
    return render(request, "articles/detail.html", context=context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    context = {}
    context["article"] = article
    return render(request, "articles/update.html", context=context)

def update_proc(request, pk):
    title = request.POST.get("title")
    content = request.POST.get("content")
    article = Article.objects.get(pk=pk)
    article.title = title
    article.content = content
    article.save()

    return redirect("/")

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect("/")
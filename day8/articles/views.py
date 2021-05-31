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

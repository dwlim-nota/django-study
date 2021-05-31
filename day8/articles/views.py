from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    return render(request, "articles/index.html")

def create(request):
    return render(request, "articles/create.html")

def create_proc(request):
    title = request.POST.get("title")
    content = request.POST.get("content")
    Article.objects.create(title=title, content=content)
    return redirect("/")

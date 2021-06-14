from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import get_user, login, logout, authenticate
from .models import Page

# Create your views here.
def index(request):
    pages = Page.objects.all()
    context = {"pages": pages}
    return render(request, 'pages/index.html', context)

def create(request):
    if request.method == "POST":
        ip_addr = request.META.get('REMOTE_ADDR')
        title = request.POST.get("title")
        content = request.POST.get("content")
        if request.user.is_authenticated:
            user = request.user
        else:
            user = None
        Page.objects.create(title=title, content=content, ip_addr=ip_addr, author=user)
        return redirect("pages:index")
    else:
        return render(request, "pages/create.html")

def detail(request, pk: int):
    page = Page.objects.get(pk=pk)
    comments = page.comments.all() # page.comment_set.all()
    context = {"page": page, "comments": comments}
    return render(request, 'pages/detail.html', context)

def update(request, pk: int):
    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect("pages:index")
        title = request.POST.get("title")
        content = request.POST.get("content")

        page = Page.objects.get(pk=pk)
        page.title = title
        page.content = content
        page.save()
        return redirect("pages:index")
    else:
        page = Page.objects.get(pk=pk)
        context = {"page": page}
        return render(request, "pages/update.html", context)

def delete(request, pk: int):
    page = Page.objects.get(pk=pk)
    page.delete()
    return redirect('pages:index')

def create_comment(request, page_pk: int):
    pass
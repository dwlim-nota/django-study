from django.shortcuts import render, redirect
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
        Page.objects.create(title=title, content=content, ip_addr=ip_addr)
        return redirect("pages:index")
    else:
        return render(request, "pages/create.html")

def detail(request, pk: int):
    page = Page.objects.get(pk=pk)
    context = {"page": page}
    return render(request, 'pages/detail.html', context)

def update(request, pk: int):
    if request.method == "POST":
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
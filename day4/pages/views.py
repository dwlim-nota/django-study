from django.shortcuts import render

# Create your views here.
def throw(request):
    return render(request, "pages/throw.html")

def catch(request):
    message = request.GET.get("message")
    message1 = request.GET.get("message1")
    context = {}
    context["message"] = message
    context["message1"] = message1
    return render(request, "pages/catch.html", context)
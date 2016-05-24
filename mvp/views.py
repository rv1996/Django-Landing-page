from django.shortcuts import render

# Create your views here.

def home(request):
    title = "Home Page"

    context_variable = {
        "template_title":title
    }
    return render(request,'mvp/home.html',context_variable)
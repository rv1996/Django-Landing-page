from django.shortcuts import render

# Create your views here.
from .forms import SignUpForm
def home(request):

    if request.user.is_authenticated():
        title = "Home|{}".format(request.user)
    else :
        title = "Home"
    form = SignUpForm()
    context_variable = {
        "template_title": title,
        "form": form,
    }

    #add a form


    if request.method == "POST":
        form = SignUpForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            context_variable = {
                "title": title,
                "comment": "Thank you submitting",
            }
            print (instance.email)
            print (instance.timestamp)
            print (instance.full_name)
            print ("form is valid")

        print("POST call ")


    return render(request,'mvp/home.html',context_variable)
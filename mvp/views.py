from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
from .forms import SignUpForm,ContactForm


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

    # add a form

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

    return render(request, 'mvp/home.html', context_variable)


def contact(request):
    form = ContactForm(request.POST or None)
    context_variable ={
        "form": form,
    }

    if request.method == "POST":
        print("POST")
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form_email = form.cleaned_data.get('email')
            form_message = form.cleaned_data.get('message')
            form_full_name = form.cleaned_data.get('full_name')

            subject = "Website contact Form"
            contact_message = """
            {}:{} via {}
            """.format(form_full_name, form_message, form_email)
            from_email = settings.EMAIL_HOST_USER
            to_email = from_email

            send_mail(subject,
                      contact_message,
                      from_email,
                      to_email,
                      html_message="<h1>Hello this failed</h1>",
                      fail_silently=False)

            # print("form is valid")
            # print (email,message,full_name1)

    return render(request, "mvp/forms.html", context_variable)

from django.contrib import admin

# Register your models here.
from .models import SignUp

from .forms import SignUpForm
#we can even add the form class into django admin and customize the admin panel of a django

class SignUpAdmin(admin.ModelAdmin):
    # class meta:
    #     model = SignUp
    list_display = ['email', 'full_name', 'timestamp', 'updated']
    form = SignUpForm
    # list_editable = ['email']


admin.site.register(SignUp, SignUpAdmin)

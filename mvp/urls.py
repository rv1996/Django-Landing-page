from django.conf.urls import url
from . import views

app_name = 'mvp'

urlpatterns = [
    url(r'^home/$',views.home,name="home"),
]
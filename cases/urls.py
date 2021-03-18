from django.conf.urls import url, include
from .views import cases

urlpatterns = [
    url(r'^$', cases, name='cases'),       
]
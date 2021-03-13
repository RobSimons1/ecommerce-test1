from django.conf.urls import url, include
from .views import downloads

urlpatterns = [
    url(r'^$', downloads, name='downloads'),       
]
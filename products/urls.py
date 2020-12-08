from django.conf.urls import url, include
from .views import products

urlpatterns = [
    url(r'^$', products, name='products'),
]
from django.conf.urls import url, include
from .views import products
from user_ratings.views import get_review_list, create_an_item

urlpatterns = [
    url(r'^$', products, name='products'),
    url(r'^get_review_list/(?P<id>\d+)', get_review_list, name="get_review_list"), 
    url(r'^add/$', create_an_item, name="create_an_item"), # user_ratings urls import
]
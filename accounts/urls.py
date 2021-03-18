from django.conf.urls import url, include
from . import urls_reset
from .views import index, register, profile, logout, login, contact, downloads, about, cases

urlpatterns = [
    url(r'^contact/$', contact, name='contact'),
    url(r'^downloads/$', downloads, name='downloads'),
    url(r'^about/$', about, name='about'),
    url(r'^cases/$', about, name='cases'),
    url(r'^register/$', register, name='register'),
    url(r'^profile/$', profile, name='profile'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^login/$', login, name='login'),
    url(r'^password-reset/', include(urls_reset)),
]
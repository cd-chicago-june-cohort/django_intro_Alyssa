from django.conf.urls import url
from views import index, new, register, login

urlpatterns = [
    url(r'^$', index),
    url(r'^new$', new),
    url(r'^register$', register), 
    url(r'^login$', login),
]
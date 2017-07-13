from django.conf.urls import url
from views import index, new, create, show, edit, destroy

urlpatterns = [
    url(r'^$', index),
    url(r'^new$', new),
    url(r'^create$', create),
    url(r'^(?P<number>\d+)$', show),
    url(r'^(?P<number>\d+)/edit', edit),
    url(r'^(?P<number>\d+)/delete', destroy),
]
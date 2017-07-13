from django.conf.urls import url
from views import index, new

urlpatterns = [
    url(r'^$', index),
    url(r'^new$', new),
]
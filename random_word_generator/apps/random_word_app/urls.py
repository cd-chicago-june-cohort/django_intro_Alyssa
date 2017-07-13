from django.conf.urls import url
from views import index, reset

urlpatterns = [
    url(r'^$', index),
    url(r'^reset$', reset),
]
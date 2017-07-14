from django.conf.urls import url
from views import index, buy, checkout

urlpatterns = [
    url(r'^$', index),
    url(r'^buy/(?P<product_id>\d+)$', buy),
    url(r'^checkout$', checkout),
]
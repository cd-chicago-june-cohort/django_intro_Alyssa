from django.conf.urls import url
from views import index, process_money

urlpatterns = [
    url(r'^$', index),
    url(r'^process_money/(?P<location>[A-z]+)', process_money),
]

from django.conf.urls import url

from .views import StatusAPIView, StatusAPIDetailView

app_name = "StatusAPI"


urlpatterns = [
    url(r'^$', StatusAPIView.as_view(), name='list'),
    url(r'^(?P<id>\d+)/$', StatusAPIDetailView.as_view(), name='detail'),
]

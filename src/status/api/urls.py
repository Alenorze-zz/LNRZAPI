from django.conf.urls import url

from .views import StatusAPIView, StatusAPIDetailView

app_name = "StatusAPI"


urlpatterns = [
    url(r'^$', StatusAPIView.as_view()),
    url(r'^(?P<id>\d+)/$', StatusAPIDetailView.as_view()),
    url(r'^(?P<id>\d+)/$', StatusAPIDetailView.as_view(), name='detail'),
]

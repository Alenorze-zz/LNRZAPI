from django.conf.urls import url

from .views import StatusAPIView, StatusCreateAPIView


urlpatterns = [
    url(r'^$', StatusAPIView.as_view()),
    url(r'^create/$', StatusCreateAPIView.as_view()),
]

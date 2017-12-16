from django.conf.urls import url
from django.contrib import admin

from updates.views import JsonCBV, JsonCBV2
  

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^json/cbv/$', JsonCBV.as_view()),
    url(r'^json/cbv2/$', JsonCBV2.as_view()),
]

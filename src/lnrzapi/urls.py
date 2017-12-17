from django.conf.urls import url, include
from django.contrib import admin

from updates.views import (
            json_example_view, 
            JsonCBV, 
            JsonCBV2, 
            SerializedDetialView, 
            SerializedListView
    )

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/updates/', include('updates.api.urls')),
]

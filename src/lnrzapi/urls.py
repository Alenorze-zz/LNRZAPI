from django.conf.urls import url, include
from django.contrib import admin

from rest_framework_jwt.views import refresh_jwt_token, obtain_jwt_token


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/auth/', include('accounts.api.urls', namespace='api-auth')),
    url(r'^api/user/', include('accounts.api.user.urls', namespace='api-user')),
    url(r'^api/status/', include('status.api.urls', namespace='api-status')),
    url(r'^api/postings/', include('postings.api.urls', namespace='api-postings')),
]

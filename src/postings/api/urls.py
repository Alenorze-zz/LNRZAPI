from django.conf.urls import url

from rest_framework_jwt.views import obtain_jwt_token

from .views import BlogPostRUDView

app_name = 'RUDPost'


urlpatterns = [
    url(r'^(?P<pk>\d+)/$', BlogPostRUDView.as_view(), name='post-rud'),
    url(r'^api/auth/login/$', obtain_jwt_token, name='api-login'),
]

from django.conf.urls import url

from .views import BlogPostRUDView


app_name = 'RUDPost'


urlpatterns = [
    url(r'^(?P<pk>\d+)/$', BlogPostRUDView.as_view(), name='post-rud')
]

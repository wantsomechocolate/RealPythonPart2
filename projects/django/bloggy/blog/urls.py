from django.conf.urls import patterns, include, url
from blog import views

urlpatterns = patterns('',

    url(r'^$', views.index, name='index'),
    url(r'^add_post/$',views.add_post, name='add_post'),
    url(r'^(?P<post_name>\w+)/$',views.post, name='post'),

)
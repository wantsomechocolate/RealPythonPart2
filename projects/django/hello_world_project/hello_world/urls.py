from django.conf.urls import patterns, include, url
from hello_world import views

urlpatterns = patterns('hello_word.views',
    # Examples:
    # url(r'^$', 'hello_world_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^better/$', views.better, name='better'),
)
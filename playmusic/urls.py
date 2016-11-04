from django.conf.urls import url

from . import views

urlpatterns = [
	#http://localhost:8000/playmusic/
    url(r'^$', views.index, name='index'),

    #http://localhost:8000/playmusic/search/search_term
    #[\w\-]+
    url(r'^search/(?P<q>.*)/$', views.search, name='search'),

    url(r'^add/(?P<q>(\d+))/$', views.add, name='add'),

    url(r'^pause$', views.pause, name='pause'),

    url(r'^play$', views.play, name='play'),

    url(r'^skip$', views.skip, name='skip'),

    url(r'^prev$', views.prev, name='prev'),

    url(r'^delete/(?P<q>(\d+))/$', views.delete, name='delete'),

    url(r'^poll$', views.poll, name='poll'),
]
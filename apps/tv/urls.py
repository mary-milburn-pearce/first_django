from django.conf.urls import url

from . import views		                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^shows$', views.all_shows),
    url(r'^shows/(?P<show_id>\d+)$', views.display_show),
    url(r'^shows/new$', views.new_show),
    url(r'^shows/create$', views.create_show),
    url(r'^shows/(?P<show_id>\d+)/edit$', views.edit_show),
    url(r'^shows/(?P<show_id>\d+)/update$', views.update_show),
    url(r'^shows/(?P<show_id>\d+)/destroy$', views.delete_show),
]
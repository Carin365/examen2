from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
	url(r'^$','main.views.home', name='home'),
	url(r'^zombie/(?P<pk>\d+)$', 'main.views.show_zombie', name='show_zombie'),

	url(r'^zombie/(?P<pk>\d+)/edit$', 'main.views.edit_zombie', name='edit_zombie'),
	url(r'^tweet/(?P<pk>\d+)/edit$', 'main.views.edit_tweet', name='edit_tweet'),
	url(r'^zombie/(?P<pk>\d+)/delete$', 'main.views.delete_zombie', name='delete_zombie'),
	url(r'^tweet/(?P<pk>\d+)/delete$', 'main.views.delete_tweet', name='delete_tweet'),
	url(r'^zombie/add/$', 'main.views.add_zombie', name='add_zombie' ),
	url(r'^tweet/add/$', 'main.views.add_tweet', name='add_tweet' ),

)

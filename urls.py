from django.conf.urls.defaults import *
from django.contrib import admin
from mysite.books import views
admin.autodiscover()

urlpatterns = patterns('',
	(r'^hello/$', 'mysite.views.hello'),
	(r'^ex1/$', 'mysite.views.exercise1'),
	(r'^time/$', 'mysite.views.current_datetime'),
	('^$', 'mysite.views.hello'),
	#
	(r'^mypage/$', 'mysite.views.my_page'),
	(r'^time/plus/(\d{1,2})/$', 'mysite.views.hours_ahead'),
	(r'^admin/', include(admin.site.urls)),
	#
	(r'^search-form/$', views.search_form),
	(r'^search/$', views.search),
	(r'^contact/$', views.contact),
	#(r'^thanks/$', views.contact),
)

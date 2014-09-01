from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'getqapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^$', 'quickfeedback.views.index'),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^login/$', 'quickfeedback.views.user_login'),
	url(r'logout/$', 'quickfeedback.views.user_logout'),
	url(r'^register/$', 'quickfeedback.views.register'),
	url(r'^createq/$', 'quickfeedback.views.createq'),
	url (r'^(?P<qid>\w+)/$', 'quickfeedback.views.qform'),
)

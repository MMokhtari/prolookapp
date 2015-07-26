from django.conf.urls import patterns, url
# from rest_framework.urlpatterns import format_suffix_patterns # for handeling the .jason or any other (format = None)
from home import views

urlpatterns = patterns('',
    url(r'^$', views.home,name='home'),
    url(r'^login/$', views.login,name='login'),
    url(r'^logout/$', views.logout,name='logout'),
    url(r'^signup/$', views.signup,name='signup')
    )

# urlpatterns = format_suffix_patterns(urlpatterns)

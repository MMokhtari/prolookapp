from django.conf.urls import patterns, url
# from rest_framework.urlpatterns import format_suffix_patterns # for handeling the .jason or any other (format = None)
from companymanager import views

urlpatterns = patterns('',
    url(r'^WorkPlace/CompanyManager/$', views.companymanager,name='companymanager'),
    )

# urlpatterns = format_suffix_patterns(urlpatterns)

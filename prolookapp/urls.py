from django.conf.urls import patterns, url, include
from rest_framework import routers
from quickstart import views
from AuthAccount.views import AccountViewSet
from taskmanager.views import TaskViewSet
# from myuser.models import User,UserManager

# from django.conf.urls import patterns, include, url
# from django.contrib import admin

# router_ = routers.SimpleRouter()
# router_.register(r'accounts', AccountViewSet)

router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)

router.register(r'accounts', AccountViewSet)
router.register(r'tasks', TaskViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.

handler404 = 'home.views.handler404'

urlpatterns = patterns('',
    url(r'^api/',include(router.urls)),
    url(r'^', include('home.urls')),
    url(r'^', include('companymanager.urls')),
    url(r'^', include('employeesmanager.urls')),
    url(r'^', include('taskmanager.urls')),
    url(r'^', include('workplace.urls')),
    url(r'^api/', include('snippets.urls')),
    url(r'^api-auth/', include('rest_framework.urls',namespace='rest_framework')),
    # url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    # url('^.*$', IndexView.as_view(), name='index'),
     )


# urlpatterns = patterns('',
# Examples:
# url(r'^$', 'prolookapp.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

#                        url(r'^admin/', include(admin.site.urls)),
# url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
#                        )
# from django.conf.urls import url, patterns, include
# from django.contrib.auth.models import User, Group
# from rest_framework import viewsets, routers
# ViewSets define the view behavior.


# class UserViewSet(viewsets. ModelViewSet):
#     model = User


# class GroupViewSet(viewsets. ModelViewSet):
#     model = Group
# Routers provide an easy way of automatically determining the URL conf.
#     router = routers. DefaultRouter()
#     router. register(r' users', UserViewSet)
#     router. register(r' groups', GroupViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token
from masterdata import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'millrest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', obtain_jwt_token),
    url(r'^index/$', views.SnippetList.as_view()),
    url(r'^restricted/$', views.RestrictedView.as_view()),

    url(r'^profile/list/(?P<model>.*)/$', 'masterdata.jsonviews.ListCFeed'),
    url(r'^profile/add/(?P<model>.*)/$', 'masterdata.jsonviews.AddCFeed'),
    url(r'^profile/edit/(?P<model>.*)/(?P<object_id>.*)/$',
    'masterdata.jsonviews.EditCFeed'),
    url(r'^profile/active/(?P<model>.*)/(?P<object_id>.*)/$',
    'masterdata.jsonviews.ActiveCFeed'),



]

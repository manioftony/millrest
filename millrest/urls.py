from django.conf.urls import include, url
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token
from masterdata import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'millrest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^index/$', views.SnippetList.as_view()),
    url(r'^restricted/$', views.RestrictedView.as_view()),


]

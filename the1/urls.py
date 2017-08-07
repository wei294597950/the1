"""the1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from one import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/$',views.index,name='index'),
    url(r'^che/', views.che ,name="che"),
    # url(r'^test3/', views.test3 ,name="test3"),
    url(r'^listing/$', views.listing, name='listing'),
    url(r'^tools/$', views.tools, name='tools'),
url(r'^form_edit/$', views.form_edit, name='form_edit'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
url(r'^logout/$',views.logout,name='logout'),
    url(r'^django_ajax/', views.django_ajax ,name="django_ajax")

]

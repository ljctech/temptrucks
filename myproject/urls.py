"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import include, url
from django.contrib import admin
from myproject import views

from django.contrib.auth.views import login, logout, password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from django.urls import path
admin.autodiscover()
import debug_toolbar
# import hello.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [

    path('admin/', admin.site.urls),
    url(r'^$', views.login_redirect, name = 'login_redirect'),
    url(r'^saferdb/', include('saferdb.urls', namespace='saferdb')),
    url(r'^accounts/', include('accounts.urls', namespace='accounts') ),
    url(r'^reset-password/$', password_reset, name='reset_password'),
    url(r'^reset-password/done/$', password_reset_done, name='password_reset_done'),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        password_reset_confirm, name = 'password_reset_confirm'),
    url(r'^reset-password/complete/$', password_reset_complete, name='password_reset_complete'),
    path(r'__debug__', include(debug_toolbar.urls))

]

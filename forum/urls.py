"""forum URL Configuration

The `urlpatterns` list routes URLs to topic_views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function topic_views
    1. Add an import:  from my_app import topic_views
    2. Add a URL to urlpatterns:  path('', topic_views.home, name='home')
Class-based topic_views
    1. Add an import:  from other_app.topic_views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myforum import topic_views
from django.conf.urls import url, include

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'',include('myforum.urls')),
]
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

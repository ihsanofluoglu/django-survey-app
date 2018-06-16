"""aliTask1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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

from task1app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^question/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^question/new/$', views.QuestionView.as_view(), name='new'),
    url(r'^question/(?P<pk>[0-9]+)/new/$', views.ChoiceView.as_view(), name='choice'),

    #url(r'^question/(?P<pk>[0-9]+)/choice/$', views.ChoiceView.as_view(), name='answer'),
    url(r'^question/(?P<pk>[0-9]+)/delete/$', views.DeleteView.as_view(), name='delete'),
    url(r'^question/(?P<pk>[0-9]+)/choice/(?P<id>[0-9]+)/delete/$', views.DeleteViewChoice.as_view(), name='delete-choice'),
    url(r'^question/(?P<pk>[0-9]+)/vote/$', views.VoteView.as_view(), name='vote'),
]

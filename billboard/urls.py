from django.conf.urls import url, include
from . import views
from django.contrib.auth import views as authviews

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^submit_message$', views.get_new_entry),
    url(r'^delete_message$', views.delete_entry),
    url(r'^signup/$', views.signupform),
    url(r'^newusercreated/$', views.newUserCreated),
    url(r'^login/$', authviews.login, name='login'),
    url(r'^logout/$', authviews.logout, {'next_page': '/billboard'}, name='logout'),
]

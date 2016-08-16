from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^signin$', views.signin),
    url(r'^login$', views.login),
    url(r'^signup$', views.signup),
    url(r'^register$', views.register),
    url(r'^users/show/(?P<id>\d+)$', views.show),
    url(r'^submitmessage$', views.submitMessage),
    url(r'^postcomment$', views.postComment),
    url(r'^dashboard$', views.dashboard),
    url(r'^dashboard/admin$', views.adminDash),
    url(r'^users/edit/(?P<id>\d+)$', views.edit),
    url(r'^remove/(?P<id>\d+)$', views.remove),
    url(r'^users/new$', views.new),
    url(r'^create$', views.create),
    url(r'^update$', views.update),
    url(r'^users/changepass$', views.changePass),
    url(r'^users/edit$', views.profile),
    url(r'^description$', views.description),
]

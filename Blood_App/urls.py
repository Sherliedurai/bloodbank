from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^registration/$',views.registration,name='registration'),
    url(r'^login/$',views.userLogin,name='login'),
    url(r'^home/$',views.home,name='home'),
    url(r'^request/(?P<pk>\d+)/$',views.requestblood,name='request'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^admin/$', views.blood_bank_admin, name='admin'),
    url(r'^issue/(?P<pk>\d+)/$', views.issue_blood, name='issue'),
    url(r'^donate/$',views.donate_blood,name='donate'),
]
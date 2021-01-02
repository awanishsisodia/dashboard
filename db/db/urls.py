from django.contrib import admin
from django.urls import path
from django.conf import settings
from app import views
from django.contrib.auth.views import LoginView,LogoutView
from django.conf.urls.static import static
from django.views.static import serve
from django.conf.urls import url

urlpatterns = [

    path('admin/', admin.site.urls),
    path('',views.home_view,name=''),
    path('afterlogin', views.afterlogin_view,name='afterlogin'),
    path('logout', LogoutView.as_view(template_name='db/logout.html'),name='logout'),
    path('send-feedback', views.send_feedback_view,name='send-feedback'),
    path('camera-dashboard', views.cameradashveiw,name='camera-dash'),
    path('view-customer', views.view_customer_view,name='view-customer'),
    path('delete-customer/<int:pk>', views.delete_customer_view,name='delete-customer'),
    path('update-customer/<int:pk>', views.update_customer_view,name='update-customer'),
    path('customersignup', views.customer_signup_view),
    path('customerlogin', LoginView.as_view(template_name='db/customerlogin.html'),name='customerlogin'),
    path('customer-home', views.customer_home_view,name='customer-home'),
    path('my-profile', views.my_profile_view,name='my-profile'),
    path('edit-profile', views.edit_profile_view,name='edit-profile'),
############################################################################################
    path('cust-home',views.cust_home_view,name="cust-home"),
    path('bang-camera-dashboard',views.ban_cameradashveiw,name='camera-ban'),
##############################################################################################
    path('new-user',views.new_user,name="new-user"),
    path('wait',views.wait,name='wait'),
    path('loc-three',views.location3,name='loaction'),
    path('locthree-camdash',views.location3cameradashveiw,name="camthree"),
#############----------- is_location4--------------###########################################
    path('loc-four',views.location4,name='loaction-4'),
    path('locfour-camdash',views.location4cameradashveiw),
#############----------- is_location5--------------###########################################
    path('loc-five',views.location5,name='loaction-5'),
    path('locfive-camdash',views.location5cameradashveiw),
#############----------- is_location6--------------###########################################
    path('loc-six',views.location6,name='loaction-6'),
    path('locsix-camdash',views.location6cameradashveiw),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

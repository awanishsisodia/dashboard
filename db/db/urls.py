from django.contrib import admin
from django.urls import path
from app import views
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [

    path('admin/', admin.site.urls),
    path('home',views.home_view,name=''),

    path('afterlogin', views.afterlogin_view,name='afterlogin'),
    path('logout', LogoutView.as_view(template_name='db/logout.html'),name='logout'),
    path('aboutus', views.aboutus_view),
    path('contactus', views.contactus_view,name='contactus'),
#    path('search', views.search_view,name='search'),
    path('send-feedback', views.send_feedback_view,name='send-feedback'),
    path('view-feedback', views.view_feedback_view,name='view-feedback'),

    path('adminclick', views.adminclick_view),
    path('adminlogin', LoginView.as_view(template_name='db/adminlogin.html'),name='adminlogin'),
    path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),
    path('camera-dashboard', views.cameradashveiw,name='CameraDashboard'),

    path('view-customer', views.view_customer_view,name='view-customer'),
   path('delete-customer/<int:pk>', views.delete_customer_view,name='delete-customer'),
    path('update-customer/<int:pk>', views.update_customer_view,name='update-customer'),
#    path('import_sheet/', views.import_sheet, name="import_sheet"),

#    path('admin-products', views.admin_products_view,name='admin-products'),
#    path('admin-add-product', views.admin_add_product_view,name='admin-add-product'),
#    path('delete-product/<int:pk>', views.delete_product_view,name='delete-product'),
#    path('update-product/<int:pk>', views.update_product_view,name='update-product'),

#    path('admin-view-booking', views.admin_view_booking_view,name='admin-view-booking'),
#    path('delete-order/<int:pk>', views.delete_order_view,name='delete-order'),
#    path('update-order/<int:pk>', views.update_order_view,name='update-order'),


    path('customersignup', views.customer_signup_view),
    path('', LoginView.as_view(template_name='db/customerlogin.html'),name='customerlogin'),
    path('customer-home', views.customer_home_view,name='customer-home'),
    #path('my-order', views.my_order_view,name='my-order'),
    path('my-profile', views.my_profile_view,name='my-profile'),
    path('edit-profile', views.edit_profile_view,name='edit-profile'),


]
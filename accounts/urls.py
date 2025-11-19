from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('product/', views.product_list, name='product_list'),
    path('products/phones/', views.phones_list, name='phones_list'),
    path('products/appliances/', views.appliances_list, name='appliances_list'),
    path('logout/', views.logout_view, name='logout'),
]

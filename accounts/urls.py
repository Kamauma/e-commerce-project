from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('product/', views.product_list, name='product_list'),
    path('logout/', views.logout_view, name='logout'),
]

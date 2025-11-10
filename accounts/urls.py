#home.html
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]


#login.html
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('product/', views.product_list, name='product_list'),
]

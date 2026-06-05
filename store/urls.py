from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('shops/', views.shop_list, name='shop_list'),
    path('shops/create/', views.shop_create, name='shop_create'),
    path('shops/<slug:slug>/', views.shop_detail, name='shop_detail'),
    path('products/', views.product_list, name='product_list'),
    path('products/<slug:slug>/', views.product_detail, name='product_detail'),
    path('products/<slug:slug>/edit/', views.product_edit, name='product_edit'),
    path('products/<slug:slug>/delete/', views.product_delete, name='product_delete'),
    path('shops/<slug:shop_slug>/add-product/', views.product_create, name='product_create'),
    path('category/<slug:slug>/', views.category_filter, name='category_filter'),
]

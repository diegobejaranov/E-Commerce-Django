from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    # Catálogo principal 
    path('', views.product_list, name='product_list'),
    
    # Catálogo filtrado por categoría
    path('category/<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    
    # Detalle de producto
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    
    # Carrito de compras
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('cart/remove/<int:product_id>/', views.cart_remove, name='cart_remove'),

    # Rutas para sumar y restar cantidades
    path('cart/increment/<int:product_id>/', views.cart_increment, name='cart_increment'),
    path('cart/decrement/<int:product_id>/', views.cart_decrement, name='cart_decrement'),
    
    # Pedidos
    path('order/create/', views.order_create, name='order_create'),
    path('order/my-orders/', views.order_list, name='order_list'),
    
    # Autenticación de la tienda
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
]


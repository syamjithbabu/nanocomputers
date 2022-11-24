from django.urls import path
from . import views

app_name= 'web'

urlpatterns = [
    path('',views.index,name="index"),
    path('about',views.about,name="about"),
    path('blog',views.blog,name="blog"),
    path('blog-details/<int:id>/',views.blog_details,name="blog-details"),
    path('shop',views.shop,name="shop"),
    path('contact',views.contact,name="contact"),
    path('cart',views.cart,name="cart"),
    path('checkout',views.checkout,name="checkout"),
    path('checkout/<int:id>/',views.checkout,name="checkout"),
    path('single-product/<int:id>/',views.single_product,name="single-product"),
    path('single-product',views.single_product,name="single-product"),
    path('add-cart/<int:product_id>/',views.add_cart,name="add_cart"),
    path('remove-cart/<int:product_id>/',views.remove_cart,name="remove_cart"),
    path('remove-cart-item/<int:product_id>/',views.remove_cart_item,name="remove_cart_item"),
]
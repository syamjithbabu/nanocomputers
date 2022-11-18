from contextlib import redirect_stderr
from django.shortcuts import render, redirect ,get_object_or_404
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from web.models import Banner, Category, Product, SpecialOffer, Blog, Team, Feedback, Ad, SubCategory, Cart, CartItem

# Create your views here.

def index(request):
    banner_product = Banner.objects.filter().all()
    category = Category.objects.filter().all()
    products = Product.objects.filter().all()[:4]
    offers = SpecialOffer.objects.filter().all()[:1]
    feedback = Feedback.objects.filter().all()
    ads = Ad.objects.filter().all()[:2]
    context = {
        'banner_product' : banner_product,
        'category' : category,
        'products' : products,
        'offers' : offers,
        'feedback' : feedback,
        'ads' : ads
    }
    return render(request,'web/index.html',context)

def about(request):
    team = Team.objects.filter().all()
    context = {
        'team' : team
    }
    return render(request,'web/about-us.html',context)

def blog(request):
    blog = Blog.objects.filter().all()
    context = {
        'blog' : blog
    }
    return render(request,'web/blog-grid.html',context)
    
def blog_details(request,id):
    blog = Blog.objects.get(id=id)
    context = {
        'blog' : blog
    }
    return render(request,'web/blog-details.html',context)

def shop(request):
    products = Product.objects.filter().all()
    subcategory = SubCategory.objects.filter().all()
    context = {
        'products' : products,
        'subcategory' : subcategory
    }
    return render(request,'web/shop.html',context)

def contact(request):
    return render(request,'web/contact.html')


def single_product(request,id):
    product = Product.objects.get(id=id)
    print(product.product_name)
    context = {
        'product' : product
    }
    return render(request,'web/single-product.html',context)

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request,product_id):
    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
        )
    cart.save()

    try:
        cart_item = CartItem.objects.get(item=product,cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            item = product,
            quantity = 1,
            cart = cart
        )
        cart_item.save()
    return redirect('web:cart')

def remove_cart(request,product_id):
    cart = Cart.objects.get(cart_id = _cart_id(request))
    product = get_object_or_404(Product,id=product_id)
    cart_item = CartItem.objects.get(item=product,cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('web:cart')

def remove_cart_item(request,product_id):
    cart = Cart.objects.get(cart_id = _cart_id(request))
    product = get_object_or_404(Product,id=product_id)
    cart_item = CartItem.objects.get(item=product,cart=cart)
    cart_item.delete()
    return redirect('web:cart')

def cart(request,total=0,quantity=0,cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active =True)
        for cart_item in cart_items:
            total  += (cart_item.item.product_price * cart_item.quantity)
            quantity += cart_item.quantity
    except ObjectDoesNotExist:
        pass
    context = {
        'total' : total,
        'quantity' : quantity,
        'cart_items' : cart_items
    }
    print(total)
    return render(request,'web/cart.html',context)

def checkout(request,total=0,quantity=0,cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active =True)
        for cart_item in cart_items:
            total  += (cart_item.item.product_price * cart_item.quantity)
            quantity += cart_item.quantity
    except ObjectDoesNotExist:
        pass
    context = {
        'total' : total,
        'quantity' : quantity,
        'cart_items' : cart_items
    }
    print(total)
    return render(request,'web/checkout.html',context)

    
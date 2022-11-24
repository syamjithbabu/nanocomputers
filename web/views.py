from contextlib import redirect_stderr
from django.shortcuts import render, redirect ,get_object_or_404
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from web.forms import OrderForm
from web.models import Order
from web.models import Banner, Category, Product, SpecialOffer, Blog, Team, Feedback, Ad, SubCategory, Cart, CartItem, FilterPrice

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
    filter_price = FilterPrice.objects.filter().all()
    sub_id = request.GET.get('subcategories')
    price_id = request.GET.get('pricerange')
    cat_id = request.GET.get('categories')
    if sub_id:
        products = Product.objects.filter(sub_category = sub_id)
    elif price_id:
        products = Product.objects.filter(price_range = price_id)
    elif cat_id:
        products = Product.objects.filter(category = cat_id)
    else:
        products = Product.objects.filter().all()
    context = {
        'products' : products,
        'subcategory' : subcategory,
        'filter_price' : filter_price,
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
            print(total,'@'*10)
    except ObjectDoesNotExist:
        pass


    form_value = OrderForm()
    cart_items = CartItem.objects.filter(cart__cart_id=_cart_id(request))
    messagestring = ''
    data = []
    if request.method == 'POST':
        form_value = OrderForm(request.POST)
        if form_value.is_valid:
            form_value.save()
        client_name = request.POST['client_name']
        state = request.POST['state']
        district = request.POST['district']
        address = request.POST['address']
        pincode = request.POST['pincode']
        phone1 = request.POST['phone1']
        phone2 = request.POST['phone2']
        email = request.POST['email']
        cart_obj = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart_obj)
        data = []
        try:
            messagestring = 'https://wa.me/7356978603?text=Name :'+client_name+'%0aState :'+state+'%0aDistrict:'+district+'%0aAddress:'+address+'%0aPinCode:'+pincode+'%0aPhone:'+phone1+'%0aAdditional Phone:'+phone2+'%0aEmail:'+email+\
                    "%0a-----Order Details------"
            print(messagestring)
            for i in cart_items:
                data1 = {
                    'name':i.item.product_name,
                    'quantity':i.quantity,
                    'price':i.item.product_price,        
                }
                data.append(data1)
               
 
            for i in data:
                messagestring +="%0aProduct-Name:"+str(i['name'])+"%0aQuantity:"+str(i['quantity'])+"%0aPrice:"+str(i['price'])+"-----------------------------"
                messagestring+="%0a-------------------------------------------------------------"
            messagestring+="%0a-----------------------------%0a\
            Grand Total :"+str(total)+"%0a--------------------------------"
        except Exception as e:
            pass


    context = {
        'total' : total,
        'quantity' : quantity,
        'cart_items' : cart_items,
        'form' : form_value,
        'sub_total' : total,
        'link' : messagestring
    }
    return render(request,'web/checkout.html',context)


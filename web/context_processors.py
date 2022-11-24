from .models import CartItem, Cart

# def _cart_id(request):
#     cart = request.session.session_key
#     if not cart:
#         cart = request.session.create()
#     else:
#         print("0")
#     return cart

def count_cart(request):
    # if Cart.objects.get(cart_id=_cart_id(request)):
    count = CartItem.objects.filter().count()
    # else:
    #     print("0")
    return {
        'count' : count or 0,
    }
    
from .models import CartItem

def count_cart(request):
    count = CartItem.objects.all().count()
    print(count)
    return {
        'count' : count,
    }
    
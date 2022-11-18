from django.contrib import admin

from web.models import Banner,Category,SubCategory,Product,SpecialOffer,Blog,Team,Feedback,Ad,Cart,CartItem

# Register your models here.

admin.site.register(Banner)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product)
admin.site.register(SpecialOffer)
admin.site.register(Blog)
admin.site.register(Team)
admin.site.register(Feedback)
admin.site.register(Ad)
admin.site.register(Cart)
admin.site.register(CartItem)
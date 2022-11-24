from django.db import models
from versatileimagefield.fields import VersatileImageField, PPOIField

# Create your models here.

class Banner(models.Model):
    product_name = models.CharField(max_length=100,default=True)
    product_title = models.CharField(max_length=100,default=True)
    product_image = VersatileImageField('Image',upload_to = 'image/testimagemodel/')
    product_price = models.IntegerField()

    def __str__(self):
        return str(self.product_name)

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    category_image = VersatileImageField('Image',upload_to = 'image/testimagemodel/')

    def __str__(self):
        return str(self.category_name)

class SubCategory(models.Model):
    sub_category_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return str(self.sub_category_name)

class FilterPrice(models.Model):
    price_range = models.CharField(max_length=100)

    def __str__(self):
        return str(self.price_range)

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_price = models.IntegerField()
    product_old_price = models.IntegerField()
    product_image1 = VersatileImageField('Image',upload_to = 'image/testimagemodel/',ppoi_field='ppoi',null=True, blank=True)
    product_image2 = VersatileImageField('Image',upload_to = 'image/testimagemodel/',ppoi_field='ppoi',null=True, blank=True)
    product_image3 = VersatileImageField('Image',upload_to = 'image/testimagemodel/',ppoi_field='ppoi',null=True, blank=True)
    product_image4 = VersatileImageField('Image',upload_to = 'image/testimagemodel/',ppoi_field='ppoi',null=True, blank=True)
    ppoi = PPOIField('Image PPOI')
    specifications = models.CharField(max_length=1000)
    maintenance = models.CharField(max_length=1000)
    product_off = models.IntegerField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    sub_category = models.ForeignKey(SubCategory,on_delete=models.CASCADE,null=True)
    price_range = models.ForeignKey(FilterPrice,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return str(self.product_name)

class SpecialOffer(models.Model):
    offer_title = models.CharField(max_length=100)
    product_image = VersatileImageField('Image',upload_to = 'image/testimagemodel/')

    def __str__(self):
        return str("Offer")

class Blog(models.Model):
    blog_title = models.CharField(max_length=100)
    blog_image = VersatileImageField('Image',upload_to = 'image/testimagemodel/',ppoi_field='ppoi')
    ppoi = PPOIField('Image PPOI')
    blog_content = models.CharField(max_length=200)
    blogger_name = models.CharField(max_length=100)
    blogger_image = VersatileImageField('Image',upload_to = 'image/testimagemodel/')
    blog_date = models.DateField()

    def __str__(self):
        return str(self.blogger_name)

class Team(models.Model):
    employee_name = models.CharField(max_length=100)
    employee_image = VersatileImageField('Image',upload_to = 'image/testimagemodel/')
    designation = models.CharField(max_length=100)

    def __str__(self):
        return str(self.employee_name)

class Feedback(models.Model):
    username = models.CharField(max_length=100)
    user_image = VersatileImageField('Image',upload_to = 'image/testimagemodel/')
    user_role = models.CharField(max_length=100)
    feedback = models.CharField(max_length=500)

    def __str__(self):
        return str(self.username)

class Ad(models.Model):
    ad_image = VersatileImageField('Image',upload_to = 'image/testimagemodel/')
    ad_product_name = models.CharField(max_length=100)
    ad_title = models.CharField(max_length=100)
    offer_title = models.CharField(max_length=100)

    def __str__(self):
        return str(self.ad_product_name)

class Cart(models.Model):
    cart_id = models.CharField(max_length=100)
    session_key = models.CharField(max_length=100)
    products = models.ManyToManyField(Product, blank=True)
    total = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.session_key)

class CartItem(models.Model):
    item = models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,null=True,)
    is_active = models.BooleanField(default=True)
    quantity = models.PositiveIntegerField()

    def sub_total(self):
        return self.item.product_price * self.quantity
    
    def __str__(self):
        return self.item

class Order(models.Model):
    client_name = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    address = models.CharField(max_length=1000)
    pincode = models.IntegerField()
    phone1 = models.CharField(max_length=10)
    phone2 = models.CharField(max_length=10)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.client_name
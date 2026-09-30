from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
   name = models.CharField(max_length=100,unique=True)

   def __str__(self):
      return f'The new category created is {self.name}'


class Product(models.Model):
   name = models.CharField(max_length=200)
   category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
   description = models.TextField(blank=True)
   selling_price = models.DecimalField(max_digits=10, decimal_places=2)
   photo = models.ImageField(upload_to="products/", blank=True, null=True)
   is_active = models.BooleanField(default=True)
   create_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now_add=True)
   class Meta:
      ordering = ['name']

   def __str__(self):
      return f'{self.name} {self.category}'

   def get_url(self):
      return reverse('products:details',args=[self.pk])

   @property
   def quantity_of_stock(self):
      stock = getattr(self,'stock_level',None)
      return stock.quantity if stock else 0

   @property
   def is_available(self):
      return self.is_active and self.quantity_of_stock > 0

   

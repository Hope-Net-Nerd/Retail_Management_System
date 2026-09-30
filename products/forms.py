from django import forms 
from .models import Category, Product

class ProductForm(forms.ModelForm):
   initial_stock = forms.IntegerField(
      min_value=0,
      required=True,
      help_text= 'We set the amount of the starting stock.'
   )
   class Meta:
      model = Product
      fields = ['name','category','description','selling_price','image','is_active']

class CategoryForm(forms.ModelForm):
   class Meta:
      model = Category
      fields = ['name']
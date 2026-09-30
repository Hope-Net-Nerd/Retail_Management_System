from django.shortcuts import render, get_object_or_404
from .models import Product, Category 


# Create your views here.

def product_list(request):
   products = Product.objects.filter(is_active=True).select_related('category')
   category_name = request.GET.get('category')

   if category_name:
      products = products.filter(category_name=category_name)
      
   return render(request,'products/list.html',{
         'products':products,
         'categories': Category.objects.all(),}
                   )

def product_detail(request, pk):
   product = get_object_or_404(Product,pk=pk,is_active=True)
   return render(request,'products/detail.html',{'product':product})
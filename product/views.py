from typing import Any
from django.shortcuts import render , get_object_or_404
from django.views import View
from django.views.generic import TemplateView , ListView
from product.forms import ContactUsForm

from product.models import Category, Product, CommentProduct
# Create your views here.
class IndexView(TemplateView):
    template_name = "product/home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.all()
        return context

    
def detail_product(request,slug):
    product = get_object_or_404(Product,slug=slug)
    
    if request.method == "POST":
        parent_id = request.POST.get("parent_id")
        body = request.POST.get("body")
        CommentProduct.objects.create(product=product,author=request.user,body=body,parent_id=parent_id)
        
    return render(request,'product/product_detail.html',{'product':product})

        

class SearchProduct(View):
    def get(self,request):
        
        product_title = request.GET.get("title_product")
        list_products = Product.objects.filter(title__icontains=product_title) 
        return render(request,"product/home.html",{"products":list_products})
    
       
        

    


class ContectUsView(View):
    def get(self,request):
        form = ContactUsForm()
        return render(request,"product/contact.html",{'form':form})
    
    def post(self,request):
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            form = ContactUsForm()
            
        
        return render(request,"product/contact.html",{'form':form})


class FilterProductListView(ListView):
    template_name = "product/filter_product.html"
    
    model = Product
    
    context_object_name = "products"
    
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        request = self.request                                                
        
        category = request.GET.getlist('category')
        min_price = request.GET.get("min_price")
        max_price = request.GET.get("max_price")
        queryset = Product.objects.all()
        
        if category:
            queryset =  queryset.filter(category__title__in=category).distinct()
        
        if min_price and max_price:
            queryset = queryset.filter(price__lte=max_price,price__gte=min_price).distinct()
        
        context = super().get_context_data(**kwargs)
        context['recent_prods'] = Product.objects.order_by("-created","-updated")[:3]
        context['products'] = queryset
        
        return context
    
class AboutUsView(TemplateView):
    template_name = "product/about.html"

def show_categories(request,slug):
    cats = get_object_or_404(Category,slug=slug)
    list_products = cats.products.all()
    return render(request,"product/home.html",{"products":list_products})

    
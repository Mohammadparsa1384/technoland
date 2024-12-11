from django.shortcuts import redirect, render ,get_object_or_404
from django.core.mail import send_mail
from django.contrib import messages
from django.views.generic import View
import requests
import json
from django.http import HttpResponse
from accounts.models import Address
from cart.models import Order, OrderItem
from technoland import settings
from .cart import Cart
from product.models import Product

class CartDetailView(View):
    def get(self,request):
        return render(request,'cart/cart_detail.html',{})
    

class CartAddView(View):
    def post(self,request,id):
        product  = get_object_or_404(Product,id=id)

        color = request.POST.get("color","empty")
        quantity = request.POST.get("quantity", 1)
        
        if color == "empty":
            messages.error(request, "لطفا یک رنگ را انتخاب کنید")
            return redirect("product:product_detail", slug=product.slug)
        
        request.session['selected_color'] = color
        
        cart = Cart(request)
        
        cart.add(product,quantity,color,update_quantity=True)
        
        return redirect('cart:cart_detail')

class CartUpdateView(View):
    def post(self, request, item_id):
        cart = Cart(request)
        quantity = int(request.POST.get('quantity', 1))
        
        
        cart.update_quantity(item_id, quantity)
        
        return redirect("cart:cart_detail")

class CartDeleteView(View):
    def get(self,request,id):
        cart = Cart(request)
        cart.delete(id)
        return redirect("cart:cart_detail")

class CartClearView(View):
    def get(self,request):
        cart = Cart(request)
        cart.clear()
        
        return redirect("cart:cart_detail")


        

class OrderDetailView(View):
    def get(self,request,pk):
        order = get_object_or_404(Order, id=pk)
        context = {

            "order":order    
        }
        return render(request,'cart/order_detail.html',context)
    

class OrderCreationView(View):
    def get(self,request):
        cart = Cart(request)
        order = Order.objects.create(user=request.user, total_price=cart.total_price())
        for item in cart:
            OrderItem.objects.create(order=order,product=item['product'],color=item['color'],
                                     quantity=item['quantity'],price=item['price'])

        cart.clear()
        return redirect("cart:order_detail", order.id)


if settings.SANDBOX:
    
        sandbox = 'sandbox'
else:
        sandbox = 'www'

ZP_API_REQUEST = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentRequest.json"
ZP_API_VERIFY = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentVerification.json"
ZP_API_STARTPAY = f"https://{sandbox}.zarinpal.com/pg/StartPay/"

amount = 1000  # Rial / Required
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
phone = 'YOUR_PHONE_NUMBER'  # Optional
# Important: need to edit for realy server.
CallbackURL = 'http://127.0.0.1:8000/cart/verify/'

class SendRequestView(View):
    def post(self,request,pk):
        order =  get_object_or_404(Order,id=pk, user=request.user)
        address = get_object_or_404(Address,id=request.POST.get("address")) 
        order.address = f"{address.phone} - {address.address}"
        order.save()
        
        
        
        self.request.session["order_id"] =  str(order.id)
        data = {
        "MerchantID": settings.MERCHANT,
        "Amount": order.total_price,
        "Description": description,
        "Email": request.user.email,
        "CallbackURL": CallbackURL,
    }
        data = json.dumps(data)
        headers = {'content-type':'application/json','content-length':str(len(data))}
        res = requests.post(ZP_API_REQUEST,data=data,headers=headers)
        if res.status_code == 200:
            response = res.json()
            if response['Status'] == 100:
                url = f"{ZP_API_STARTPAY}{response['Authority']}"
                return redirect(url)
            pass
        else:
            print(res.json()['errors'])
            return HttpResponse(str(res.json()['errors']))

class VerifyView(View):
   def get(self,request):
       authority = request.GET.get("Authority")
       order_id = self.request.session["order_id"]
       order = get_object_or_404(Order,id=int(order_id))
       
       data = {
           
        "MerchantID": settings.MERCHANT,
        "Amount": order.total_price,
        'Authority':authority
        
       }
       data = json.dumps(data)
       headers = {'content-type':'application/json','content-length':str(len(data))}
       res = requests.post(ZP_API_VERIFY,data=data,headers=headers)
       
       if res.status_code == 200:
           response = res.json()
           if response['Status'] == 100:
            
               order.is_paid = True
               order.save()
               msg = " سفارش شما با موفقیت تایید شد به زودی جهت اطلاعات تکمیلی با شما تماس گرفته می شود"
               send_mail("خرید اینترنتی",msg,"parsajavidi17@gmail.com",[order.user.email])
               return render(request,'cart/factors.html', {'order': order}) 
           
           else:
               return render(request, "cart/order-cancel.html")
        
       
       else:
           return HttpResponse("پرداخت ناموفق بود") 
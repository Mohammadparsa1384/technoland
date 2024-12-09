from django.shortcuts import render , redirect, get_object_or_404  
from django.urls import reverse
from django.views.generic import View , ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth import login , logout, authenticate
from .forms import LoginForm , RegisterForm , AddressCreationForm
from .models import Address, Profile, User
from cart.models import Order

# Create your views here.
class LoginView(View):
    
    def get(self,request):
        form = LoginForm()
        
        return render(request,"accounts/login.html",{'form':form})
    
    def post(self,request):
        
        
        
        form = LoginForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(request,username=email,password=password)
            
            
            if user is not None:
                
                next_page = request.GET.get("next")
                if next_page:
                    login(request,user)
                    return redirect(next_page)
                
                login(request,user)
                return redirect("product:main")
            
            else:
                form.add_error("email","اطلاعات وارد شده نادرست است")
        
        return render(request,"accounts/login.html",{'form':form})


class RegisterView(View):
    def get(self,request):
        form = RegisterForm()
        return render(request,'accounts/register.html',{'form':form})
    
    def post(self,request):
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            
            user = User.objects.create(email=cd.get("email") , password=cd.get("password"))
            user.set_password(cd.get("password"))
            user.save()
            login(request,user)
            return redirect("/")
        else:
            form.add_error("email","ایمیل معتبر نیست")


        return render(request,'accounts/register.html',{'form':form})


class AddAddressView(View):
    def post(self,request):
        
        
        list_address = self.request.user.addresses.all()
        
        form = AddressCreationForm(request.POST)
        if form.is_valid() and len(list_address) < 3:
            
            address =  form.save(commit=False)
            address.user = self.request.user
            address.save()
            form = AddressCreationForm()
            
            nex_page = request.GET.get("next")
            if nex_page:
                return redirect(nex_page)
            
            
            
            
        context = {
            'form':form,
            'list_address':list_address
        }    
        
        return render(request,'accounts/address.html',context)
            
    
    def get(self,request):
        form =  AddressCreationForm()
        list_address = self.request.user.addresses.all()
        
        context = {
            'form':form,
            'list_address':list_address
        }   
        return render(request,'accounts/address.html',context)  


class AddImageUser(View):
    
    def post(self,request):
        if len(request.FILES) != 0:
            Profile.objects.create(user=self.request.user,image= request.FILES.get("profile"))
            return redirect("accounts:address")

        elif request.FILES.get("profile") == None:
            messages.error(request,"لطفا یک عکس پروفایل انتخاب کنید")
            return redirect("accounts:address")


def delete_profile(request,pk):
    profile = Profile.objects.get(id=pk)
    profile.delete()
    return redirect("accounts:address")
        
    
def delete_address(request,pk):
    
    address = Address.objects.get(id=pk)
    address.delete()
    return redirect("accounts:address")
    

def user_logout(request):
    logout(request)
    return redirect("product:main")


class UserOrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = "accounts/user_orders.html"
    context_object_name = "orders"
    
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by("-created_at")
    

class OrderDeleteView(View):
    def post(self,request,pk):
        order = get_object_or_404(Order , pk=pk)
        if not order.is_paid:
            order.delete()
            return redirect("accounts:user-orders")
            
        
    
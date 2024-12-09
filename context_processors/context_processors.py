from accounts.models import Address
from cart.cart import Cart
from cart.models import Order
from product.models import Category, Color
from django.shortcuts import get_object_or_404
def show_colors(request):
    colors = Color.objects.all()
    context = {
        'colors':colors
    }
    return context


def cart(request):
    cart = Cart(request)
    return {'cart':cart}



def list_categories(request):
    categories = Category.objects.all()
    return {"categories":categories}
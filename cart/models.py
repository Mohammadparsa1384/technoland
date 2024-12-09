from django.db import models

from accounts.models import User

from product.models import Product
# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="order",verbose_name="کاربر")
    total_price = models.BigIntegerField(default=0,verbose_name="قیمت کل")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="زمان پرداخت")
    is_paid = models.BooleanField(default=False,verbose_name="وضعیت پرداخت")
    address = models.TextField(blank=True, null=True,verbose_name="آدرس")
    
    class Meta:
        verbose_name = "سفارش"
        verbose_name_plural = "سفارش ها"
    
    def __str__(self) -> str:
        return self.user.email
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE ,related_name="items",verbose_name="سفارش")
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name="items",verbose_name="محصول")
    quantity = models.SmallIntegerField(verbose_name="تعداد")   
    color = models.CharField(max_length=12,null=True,verbose_name="رنگ") 
    price = models.PositiveIntegerField(verbose_name="قیمت")
    
    def __str__(self) -> str:
        return self.order.user.email
    
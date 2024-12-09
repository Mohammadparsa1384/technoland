from django.db import models
from django.urls import reverse
from django_jalali.db import models as jmodels
from accounts.models import User


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=15,verbose_name="عنوان")
    slug = models.SlugField(null=True)
    
    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"
    
    def get_absolute_url(self):
        return reverse("product:categories", kwargs={"slug": self.slug})
    
    
    def __str__(self) -> str:
        return self.title


class Color(models.Model):
    title = models.CharField(max_length=20,verbose_name="عنوان")
    
    class Meta:
        verbose_name = "رنگ"
        verbose_name_plural = "رنگ ها"

    def __str__(self):
        return self.title
    

class Product(models.Model):
    title = models.CharField(max_length=50,verbose_name="عنوان")
    price = models.PositiveBigIntegerField(verbose_name="قیمت")

    
    category = models.ManyToManyField(Category,related_name="products",verbose_name="دسته بندی")
    
    description = models.TextField(verbose_name="توضیحات")
    image = models.ImageField(upload_to="products",verbose_name="عکس محصول")
    quantity = models.IntegerField(default=1,verbose_name="تعداد")
    colors = models.ManyToManyField(Color,related_name="products",verbose_name="رنگ")
    slug = models.SlugField(blank=True, null=True)
    
    rate = models.IntegerField(blank=True, null=True,verbose_name="امتیاز")
    
    created = jmodels.jDateTimeField(auto_now_add=True,null=True,verbose_name="زمان ایجاد")
    updated = jmodels.jDateTimeField(auto_now=True,null=True,verbose_name="زمان آپدیت")
    objects = jmodels.jManager()
    
    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"
        ordering = ['created','updated']
    
    def get_absolute_url(self):
        return reverse("product:product_detail", kwargs={"slug": self.slug})
    
    
    def __str__(self):
        return self.title
    
class Contact(models.Model):
    subject = models.CharField(max_length=50,verbose_name="موضوع")
    message = models.TextField(verbose_name="پیام")
    
    class Meta:
        verbose_name = "تماس"
        verbose_name_plural = "تماس ها"
    def __str__(self) -> str:
        return self.message[:20]

class CommentProduct(models.Model):
    product = models.ForeignKey(Product,related_name="comments",on_delete=models.CASCADE,verbose_name="محصول")
    author = models.ForeignKey(User,related_name="comments",on_delete=models.CASCADE,verbose_name="نویسنده") 
    body = models.TextField(verbose_name="متن پیام")
    parent = models.ForeignKey("self",related_name = "replies",on_delete=models.CASCADE,blank=True, null=True)
    created = jmodels.jDateTimeField(auto_now_add=True,null=True)
    updated = jmodels.jDateTimeField(auto_now=True,null=True)
    
    def __str__(self) -> str:
        return self.body[:20]
    
    class Meta:
        verbose_name = "کامنت"
        verbose_name_plural = "کامنت ها"
    
class TeamMember(models.Model):
    image = models.ImageField(upload_to="team",verbose_name="عکس اعضا")
    name = models.CharField(max_length=30,verbose_name="نام و نام خانوادگی")
    job = models.CharField(max_length=30,verbose_name="شغل")
    desc = models.TextField(verbose_name="توضیحات")
    
    class Meta:
        verbose_name_plural = "اعضای تیم"
        verbose_name = "اعضا"
    
    def __str__(self) -> str:
        return self.job
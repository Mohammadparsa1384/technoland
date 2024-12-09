from django.db import models

from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            
            password=password,
    
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
    verbose_name="ایمیل کاربر",
    max_length=255,
    unique=True)
    
    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    # REQUIRED_FIELDS = "email"

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    
    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربران"
        
class Address(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name="addresses",verbose_name="کاربر")
      
    phone = models.CharField(max_length=12,verbose_name="تلفن تماس")
    address = models.CharField(max_length= 300,verbose_name="آدرس")
    province = models.CharField(max_length=40,null=True,verbose_name="استان")
    receiver = models.CharField(max_length=40,null=True,verbose_name="دریافت کننده")
    city = models.CharField(max_length = 40,verbose_name="شهر")
    zip_code = models.CharField(max_length=30,verbose_name="کد پستی")
    
    class Meta:
        verbose_name = "آدرس"
        verbose_name_plural = "آدرس ها"
    
    def __str__(self) -> str:
        return self.phone

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="profile",verbose_name="کاربر")
    image = models.ImageField(upload_to="profiles",blank=True, null=True,verbose_name="عکس پروفایل")
    
    def __str__(self) -> str:
        return self.user.email
    
    class Meta:
        verbose_name = "پروفایل"
        verbose_name_plural = "پروفایل ها"
from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
app_name = "accounts"

urlpatterns = [
    path("login/",views.LoginView.as_view(),name="login"),
    path("logout/",views.user_logout,name="logout"),
    
    path("register/",views.RegisterView.as_view(),name="register"),
    
    path('password-change/',auth_views.PasswordChangeView.as_view(template_name="accounts/password_change_form.html",success_url='done') , name="password_change"),
    path('password-change/done',auth_views.PasswordChangeDoneView.as_view(template_name="accounts/password_change_done_form.html"),name="password_change_done"),
    
    
    path("address/",views.AddAddressView.as_view(),name="address"),
    path("address/delete/<int:pk>",views.delete_address,name="del_add"),
    path("add-profile-image",views.AddImageUser.as_view(),name="add_user_profile"),
    path("del-profile-image/<int:pk>",views.delete_profile,name="del_user_profile"),
    path('my-orders/', views.UserOrderListView.as_view(), name='user-orders'),
    path('order/delete/<int:pk>/', views.OrderDeleteView.as_view(), name='order_delete'),
    
]

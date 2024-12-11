from . import views
from django.urls import path
app_name = "cart"
urlpatterns = [
    path('detail/',views.CartDetailView.as_view(),name="cart_detail"),
    path('add/<int:id>',views.CartAddView.as_view(),name="cart_add"),
    path('delete/<str:id>',views.CartDeleteView.as_view(),name="cart_delete"),
    path('clear/',views.CartClearView.as_view(),name="cart_clear"),
    path('order/<int:pk>',views.OrderDetailView.as_view(),name="order_detail"),
    path('order/add/',views.OrderCreationView.as_view(),name="order_create"),
    path("sendrequest/<int:pk>", views.SendRequestView.as_view(), name="send_request"),
    path("verify/",views.VerifyView.as_view(),name="verify_request"),
    path("update/<int:item_id>/", views.CartUpdateView.as_view(), name="update_qunatity")
    
    
    
]

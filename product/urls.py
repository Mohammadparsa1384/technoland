from . import views
from django.urls import path
app_name = "product"
urlpatterns = [
    path('',views.IndexView.as_view(),name="main"),
    path('product/detail/<slug:slug>',views.detail_product,name="product_detail"),
    path('product/category/<slug:slug>',views.show_categories,name="categories"),
    path('contact/',views.ContectUsView.as_view(),name="contactus"),
    path('product/filter',views.FilterProductListView.as_view(),name="filter"),
    path("product/search/",views.SearchProduct.as_view(),name="search_product"),
    path('about-us',views.AboutUsView.as_view(),name="about_us"),
    

]

from . import views
from django.urls import path
urlpatterns =[
path("", views.home, name='home'),
path("blog", views.blog, name='blog'),
path("cars", views.cars, name='cars'),
path("blog-details", views.blogDetails, name='blog-details'),
path("checkout", views.checkout, name='checkout'),
path("clothing", views.clothing, name='clothing'),
path("contact", views.contact, name='contact'),
path("furnitures", views.furnitures, name='furnitures'),
path("login", views.loginpage, name='login'),
path("products", views.products, name='products'),
path("realestate", views.realestate, name='realestate'),
path("shop-details", views.shopdetails, name='shop-details'),
path("shop-details/<str:pk>/", views.shopdetails, name='shop-details'),
path("shop-grid", views.shopGrid, name='shop-grid'),
path("shoping-cart", views.shopingCart, name='shoping-cart'),
path("shoping-cart", views.shopingCart, name='shoping-cart'),
path('update_item/', views.updateItem, name="update_item"),
path('register/', views.registerpage, name="register"),
path('logout/', views.logoutUser, name="logout"),
path('process_order/', views.processOrder, name="process_order"),

]
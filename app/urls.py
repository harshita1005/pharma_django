from django.urls import path
from app import views

urlpatterns = [
    
    path("",views.home, name='home'),
    path('medicines',views.medicines, name='medicines'),
    path('products',views.products, name='products'),
    path('orders',views.myorders, name='myorders'),
    path('contact',views.contact, name='contact'),
    path('aboutus',views.aboutus, name='aboutus'),
    path('search',views.search, name='search'),
    path('signup',views.handlesignup, name='handlesignup'),
    path('login',views.handlelogin, name='handlelogin'),
    path('logout',views.handlelogout, name='handlelogout'),
    path("orders/<id>",views.deleteOrder,name="deleteOrder"),
]

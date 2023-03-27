from django.contrib import admin

# Register your models here.
from app.models import Contact,Medicines,ProductItem,MyOrders

admin.site.register(Contact)
admin.site.register(Medicines)
admin.site.register(ProductItem)
admin.site.register(MyOrders)

from django.contrib import admin

# Register your models here.
from carts.models import Cart, CartItem


class CartAdmin(admin.ModelAdmin):
    class Meta:
        model = Cart


admin.site.register(Cart, CartAdmin)

admin.site.register(CartItem)

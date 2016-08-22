from django.contrib import admin

# Register your models here.

from .models import Product, ProductImage, Variation


class ProductImageInline(admin.StackedInline):
    model = ProductImage


class ProductAdmin(admin.ModelAdmin):
    search_fields = ['title', 'description']
    list_display = ['title', 'price', 'active', 'updated']
    list_editable = ['price', 'active']
    list_filter = ['price', 'active', 'timestamp']

    readonly_fields = ['updated', 'timestamp']
    prepopulated_fields = {"slug": ("title",)}
    inlines = [ProductImageInline]

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)

admin.site.register(ProductImage)

admin.site.register(Variation)

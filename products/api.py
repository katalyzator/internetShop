from tastypie.resources import ModelResource

from products.models import Product, ProductImage


class ProductImageResource(ModelResource):
    class Meta:
        queryset = ProductImage.objects.all()
        name = 'ProductImage'


class ProductResource(ModelResource):
    class Meta:
        queryset = Product.objects.all()
        name = 'Product'

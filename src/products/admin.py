from django.contrib import admin
from .models import Product,ProductComment,ProductCategory

admin.site.register(Product)
admin.site.register(ProductComment)
admin.site.register(ProductCategory)
from django.contrib import admin
from .models import Product,ProductComment,ProductCategory

admin.site.register(ProductComment)




class PriceRangeFilter(admin.SimpleListFilter):
    title = 'محدوده قیمت'
    parameter_name = 'price'

    def lookups(self, request, model_admin):
        return (
            ("0-100000", '0-100,000 تومان'),
            ("100001-250000", '100,001-250,000 تومان'),
            ("250001-500000", '250,001-500,000 تومان'),
            ("500001<=", '500,001 بیشتر از'),
        )
    
    def queryset(self, request, queryset):
        if self.value() == '0-100000':
            return queryset.filter(price__lte=100000)
        if self.value() == '100001-250000':
            return queryset.filter(price__range=(100001, 250000))
        if self.value() == '250001-500000':
            return queryset.filter(price__range=(250001, 500000))
        if self.value() == '500001<=':
            return queryset.filter(price__gte=500001)

@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ('title','amount','price','date')
    ordering = ('id',)
    search_fields = ('title',)
    list_filter = ('amount',PriceRangeFilter,'date')





class ProductCategoryRange(admin.SimpleListFilter):
    title = 'تعداد آیتم'
    parameter_name = 'products'

    def lookups(self, request, model_admin):
        return (
            ("0-5", '0-5 آیتم'),
            ("6-10", '6-10 آیتم'),
            ("11-20", '11-20 آیتم'),
            ("21-50",'21-50 آیتم'),
            ("51<=", '51 بیشتر از'),
        )
    
    def queryset(self, request, queryset):
        in_id = []
        if self.value() == '0-5':
            for i in queryset:
                n = i.products.all().count()
                if n <= 5:
                    in_id.append(i.id)
            return queryset.filter(pk__in=in_id)
        if self.value() == '6-10':
            for i in queryset:
                n = i.products.all().count()
                if n in range(6,11):
                    in_id.append(i.id)
            return queryset.filter(pk__in=in_id)
        if self.value() == '11-20':
            for i in queryset:
                n = i.products.all().count()
                if n in range(11,21):
                    in_id.append(i.id)
            return queryset.filter(pk__in=in_id)
        if self.value() == '21-50':
            for i in queryset:
                n = i.products.all().count()
                if n in range(21,51):
                    in_id.append(i.id)
            return queryset.filter(pk__in=in_id)
        if self.value() == '51<=':
            for i in queryset:
                n = i.products.all().count()
                if n >= 51:
                    in_id.append(i.id)
            return queryset.filter(pk__in=in_id)
            

@admin.register(ProductCategory)
class ProductCategory(admin.ModelAdmin):
    list_display = ('category_name','id')
    ordering = ('id',)
    search_fields = ('category_name',)
    list_filter = (ProductCategoryRange,)
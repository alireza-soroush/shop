from django.contrib import admin
from .models import Product,ProductComment,ProductCategory
from jalali_date import datetime2jalali


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
        elif self.value() == '100001-250000':
            return queryset.filter(price__range=(100001, 250000))
        elif self.value() == '250001-500000':
            return queryset.filter(price__range=(250001, 500000))
        elif self.value() == '500001<=':
            return queryset.filter(price__gte=500001)

class SalesRangeFilter(admin.SimpleListFilter):
    title = 'مقدار فروش'
    parameter_name = 'sales'

    def lookups(self, request , model_admin):
        return (
            ("0-10", '0-10 فروخته شده'),
            ("11-30", '11-30 فروخته شده'),
            ("31-100", '31-100 فروخته شده'),
            ("101<=", '101 بیشتر از'),
        )
    

    def queryset(self, request , queryset):
        if self.value() == '0-10':
            return queryset.filter(sales__lte = 10)
        elif self.value() == '11-30':
            return queryset.filter(sales__range = (11,30))
        elif self.value() == '31-100':
            return queryset.filter(sales__range = (31,100))
        elif self.value() == '101<=':
            return queryset.filter(sales__gte = 101)



class AmountLeftRange(admin.SimpleListFilter):
    title = 'مقدار موجود'
    parameter_name = 'amount'

    def lookups(self, request , model_admin):
        return (
            ('0-10','0-10 موجود'),
            ('11-20','11-20 موجود'),
            ('21-40','21-40 موجود'),
            ('41-100','41-100 موجود'),
            ('101<=','101 بیشتر از'),
        )
    
    def queryset(self, request , queryset):
        if self.value() == '0-10':
            return queryset.filter(amount__lte = 10)
        elif self.value() == '11-20':
            return queryset.filter(amount__range = (11,20))
        elif self.value() == '21-40':
            return queryset.filter(amount__range = (21,40))
        elif self.value() == '41-100':
            return queryset.filter(amount__range = (41,100))
        elif self.value() == '101<=':
            return queryset.filter(amount__gte = 101)



@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ('title','amount','price','sales','get_created_jalali')
    ordering = ('id',)
    search_fields = ('title',)
    list_filter = (AmountLeftRange,PriceRangeFilter,SalesRangeFilter,'date')

    @admin.display(description='تاریخ')
    def get_created_jalali(self, obj):
        return datetime2jalali(obj.date).strftime('%a, %d %b %Y %H:%M:%S')





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
        elif self.value() == '6-10':
            for i in queryset:
                n = i.products.all().count()
                if n in range(6,11):
                    in_id.append(i.id)
            return queryset.filter(pk__in=in_id)
        elif self.value() == '11-20':
            for i in queryset:
                n = i.products.all().count()
                if n in range(11,21):
                    in_id.append(i.id)
            return queryset.filter(pk__in=in_id)
        elif self.value() == '21-50':
            for i in queryset:
                n = i.products.all().count()
                if n in range(21,51):
                    in_id.append(i.id)
            return queryset.filter(pk__in=in_id)
        elif self.value() == '51<=':
            for i in queryset:
                n = i.products.all().count()
                if n >= 51:
                    in_id.append(i.id)
            return queryset.filter(pk__in=in_id)


@admin.register(ProductCategory)
class ProductCategory(admin.ModelAdmin):
    list_display = ('category_name','inside_items')
    ordering = ('id',)
    search_fields = ('category_name',)
    list_filter = (ProductCategoryRange,)




@admin.register(ProductComment)
class ProductComment(admin.ModelAdmin):
    list_display = ('user','forproduct','comment','get_created_jalali')
    ordering = ('date',)
    search_fields = ('comment','forproduct')
    list_filter = ('date','forproduct')
    
    @admin.display(description='تاریخ')
    def get_created_jalali(self, obj):
        return datetime2jalali(obj.date).strftime('%a, %d %b %Y %H:%M:%S')
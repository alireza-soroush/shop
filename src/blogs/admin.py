from django.contrib import admin
from .models import Blog,BlogComment
from jalali_date import datetime2jalali

admin.site.register(BlogComment)






class ViewsRangeFilter(admin.SimpleListFilter):
    title = 'بازدید'
    parameter_name = 'views'
    def lookups(self, request , model_admin):
        return (
            ('0-10','0-10 بازدید'),
            ('11-50','11-50 بازدید'),
            ('51-100','51-100 بازدید'),
            ('101-250','101-250 بازدید'),
            ('251-500','251-500 بازدید'),
            ('>=501','501 بیشتر از'),
        )
    
    def queryset(self, request , queryset):
        array = []
        for i in queryset.filter(blogviews__id__gte=0):
            array.append(i)
        obj_dict = {i:array.count(i) for i in array}

        in_id = []
        if self.value() == '0-10':
            for obj,views in obj_dict.items():
                if views <=10:
                    in_id.append(obj.id)
            return queryset.filter(pk__in=in_id)
        
        elif self.value() == '11-50':
            for obj,views in obj_dict.items():
                if views in range(11,51):
                    in_id.append(obj.id)
            return queryset.filter(pk__in=in_id)
        
        elif self.value() == '51-100':
            for obj,views in obj_dict.items():
                if views in range(51,101):
                    in_id.append(obj.id)
            return queryset.filter(pk__in=in_id)
        
        elif self.value() == '101-250':
            for obj,views in obj_dict.items():
                if views in range(101,251):
                    in_id.append(obj.id)
            return queryset.filter(pk__in=in_id)
        
        elif self.value() == '251-500':
            for obj,views in obj_dict.items():
                if views in range(251,501):
                    in_id.append(obj.id)
            return queryset.filter(pk__in=in_id)

        elif self.value() == '>=501':
            for obj,views in obj_dict.items():
                if views >= 501:
                    in_id.append(obj.id)
            return queryset.filter(pk__in=in_id)
        


@admin.register(Blog)
class Blog(admin.ModelAdmin):
    list_display = ('title','author','views','get_created_jalali')
    ordering = ('date',)
    search_fields = ('title','author')
    list_filter = ('date',ViewsRangeFilter,'author')


    @admin.display(description='تاریخ')
    def get_created_jalali(self, obj):
        return datetime2jalali(obj.date).strftime('%a, %d %b %Y %H:%M:%S')

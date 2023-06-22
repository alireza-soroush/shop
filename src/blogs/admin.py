from django.contrib import admin
from .models import Blog,BlogComment,BlogCategory

admin.site.register(Blog)
admin.site.register(BlogComment)
admin.site.register(BlogCategory)
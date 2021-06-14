from django.contrib import admin
from bloggapp.models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display= ['title']


    prepopulated_fields={ 'slug':('title',) }



# Register your models here.
admin.site.register(Blog,BlogAdmin)
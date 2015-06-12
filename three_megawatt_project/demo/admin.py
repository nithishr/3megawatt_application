from django.contrib import admin

# Register your models here.
from django.contrib import admin
from demo.models import Site, SiteDetail

# class SiteDetailAdmin(admin.ModelAdmin):
#    list_display = ('site.name','date','a_value','b_value')

admin.site.register(Site)
admin.site.register(SiteDetail)
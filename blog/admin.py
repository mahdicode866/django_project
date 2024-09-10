from django.contrib import admin
from blog.models import post 
# Register your models here 
class PostAdmin(admin.ModelAdmin):
    date_hierarchy="created_date"
    # date_hierarchy="name"
    empty_value_display="-empty-"
    fields=("title","content")
    # exclude=("created_date",)
    list_display=("counted_views","title","created_date","status","published_date","updated_date")
    list_filter=("status","title")
    # search_fields=("title","content")
    # ordering=("-created_date",)
    
admin.site.register(post,PostAdmin)

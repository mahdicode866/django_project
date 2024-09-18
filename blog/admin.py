from django.contrib import admin
from blog.models import post 
# Register your models here 
class PostAdmin(admin.ModelAdmin):
    date_hierarchy="created_date"
    # date_hierarchy="name"
    empty_value_display="-empty-"
    # exclude=("created_date",)
    list_display=("author","counted_views","title","created_date","status","published_date","updated_date")
    list_filter=("status","title","author")
    error_messages="hello we have error here "

    
admin.site.register(post,PostAdmin)

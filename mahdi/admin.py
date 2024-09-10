from django.contrib import admin
from mahdi.models import contact
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy="created_date"
    fields=("name",)
    search_fields="name",
    ordering=["created_date"]
    list_filter=["name","created_date"]
    list_display=["name","created_date","subject"]
admin.site.register(contact,ContactAdmin)



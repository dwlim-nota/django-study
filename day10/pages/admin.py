from django.contrib import admin
from .models import Page

# Register your models here.
class PageAdmin(admin.ModelAdmin):
    list_display = ["title", "content", "ip_addr", "created_at", "updated_at"]
    list_filter = ["ip_addr"]

admin.site.register(Page, PageAdmin)
from django.contrib import admin
from .models import Page, Comment

# Register your models here.
class PageAdmin(admin.ModelAdmin):
    list_display = ["title", "content", "ip_addr", "created_at", "updated_at"]
    list_filter = ["ip_addr"]

class CommentAdmin(admin.ModelAdmin):
    list_display = ["content", "created_at", "updated_at"]
    list_filter = ["created_at"]

admin.site.register(Page, PageAdmin)
admin.site.register(Comment, CommentAdmin)
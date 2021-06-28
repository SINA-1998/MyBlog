from django.contrib import admin
from .models import Article, Category


# Register your models here.

# For disable action use this statement 👇
# admin.site.disable_action("action name")

def make_published(modeladmin, request, queryset):
    rows_updated = queryset.update(status="p")
    if rows_updated == 1:
        message_bit = "شد."
    else:
        message_bit = "شدند."
    modeladmin.message_user(request, f"{rows_updated} مقاله منتشر {message_bit}")


def make_draft(modeladmin, request, queryset):
    rows_updated = queryset.update(status="d")
    if rows_updated == 1:
        message_bit = "شد."
    else:
        message_bit = "شدند."
    modeladmin.message_user(request, f"{rows_updated} مقاله پیش‌نویس {message_bit}")


make_published.short_description = "انتشار مقالات انتخاب شده"
make_draft.short_description = "پیش‌نویس شدن مقالات انتخاب شده"


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("position", "title", "slug", "parent", "status")
    list_filter = (["status"])
    search_fields = ("title", "slug")
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Category, CategoryAdmin)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "thumbnail_tag", "slug", "author", "jpublish", "status", "category_to_str")
    list_filter = ("publish", "status", "author")
    search_fields = ("title", "description")
    prepopulated_fields = {"slug": ("title",)}
    ordering = ["status", "publish"]
    actions = [make_published, make_draft]


admin.site.register(Article, ArticleAdmin)

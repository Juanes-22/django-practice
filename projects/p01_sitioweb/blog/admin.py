from django.contrib import admin


# Register your models here.
# from .models import Post
# admin.site.register(Post)


from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "author", "published_at", "status"]
    list_filter = ["status", "created_at", "published_at", "author"]
    search_fields = ["title", "body"]
    prepopulated_fields = {"slug": ("title",)}
    raw_id_fields = ["author"]
    date_hierarchy = "published_at"
    ordering = ["status", "published_at"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "post", "created_at", "active"]
    list_filter = ["active", "created_at", "updated_at"]
    search_fields = ["name", "email", "body"]

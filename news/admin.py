from django.contrib import admin
from .models import News

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('news_title', 'news_slug', 'news_image_preview')
    search_fields = ('news_title',)
    readonly_fields = ('news_image_preview',)

    def news_image_preview(self, obj):
        if obj.news_image:
            return f'<img src="{obj.news_image.url}" width="100" height="60" style="object-fit:cover;" />'
        return "No Image"
    news_image_preview.allow_tags = True
    news_image_preview.short_description = "Preview"

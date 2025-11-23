from django.contrib import admin
from .models import Service, Jobs

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_title', 'short_description')
    search_fields = ('service_title',)
    ordering = ('service_title',)

    def short_description(self, obj):
        return (obj.service_description[:50] + "...") if len(obj.service_description) > 50 else obj.service_description
    short_description.short_description = 'Description Preview'


@admin.register(Jobs)
class JobsAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'short_description', 'job_image_preview')
    search_fields = ('job_title',)
    ordering = ('job_title',)
    readonly_fields = ('job_image_preview',)

    def short_description(self, obj):
        return (obj.job_description[:50] + "...") if len(obj.job_description) > 50 else obj.job_description
    short_description.short_description = 'Job Desc'

    def job_image_preview(self, obj):
        if obj.job_image:
            return f'<img src="{obj.job_image.url}" width="100" height="60" style="object-fit:cover;" />'
        return "No Image"
    job_image_preview.allow_tags = True
    job_image_preview.short_description = 'Preview'

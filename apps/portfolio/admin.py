from django.contrib import admin
from django.utils.safestring import mark_safe
from apps.portfolio.models import Projects


# Register your models here.
class ProjectsAdmin(admin.ModelAdmin):
    list_display=('title', 'description', 'image_display')
    search_fields=('title', 'description', 'technology')
    list_per_page=25

    readonly_fields=['project_image']

    def project_image(self, obj):
        return mark_safe(
            '<a href="{0}"><img src="{0}" width="20%"></a>'.format(self.image.url)
        )

admin.site.register(Projects, ProjectsAdmin)
from django.db import models
from django.utils.safestring import mark_safe


# Create your models here.
class Projects(models.Model):
    title=models.CharField(max_length=200, help_text="Ingrese el título del Proyecto")
    description= models.TextField()
    technology=models.CharField(max_length=200)
    image=models.ImageField(null=True, blank=True, upload_to='img/portfolio', help_text="Seleccione una imagen para mostrar")

    def image_display(self):
        return mark_safe(
            '<a href="{0}"><img src="{0}" width="20%"></a>'.format(self.image.url)
        )
    image_display.allow_tags=True
    image_display.short_description=u'IMAGE' 
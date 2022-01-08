from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class ProjectType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default="No description available.")
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Projects Types"

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('admins:projecttype-detail', kwargs={'pk': self.pk})

from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(
        upload_to='admins/category/images/', null=True, blank=True,
        help_text='Product Category image will be displayed according to this image resolutions.'
    )
    description = models.TextField(default="No description available.")
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['-id']

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(
        upload_to='admins/tag/images/', null=True, blank=True,
        help_text='Product Category image will be displayed according to this image resolutions.'
    )
    description = models.TextField(default="No description available.")
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Tags/Keywords"
        ordering = ['-id']

    def __str__(self):
        return self.name

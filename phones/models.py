from django.db import models
from django.template.defaultfilters import slugify


class Phone(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name="Модель")
    price = models.IntegerField(verbose_name="Цена")
    image = models.URLField(verbose_name="Изображение")
    release_date = models.DateField(verbose_name="Дата выхода")
    lte_exists = models.BooleanField(verbose_name="Наличие LTE")
    slug = models.SlugField(max_length=255, blank=True, unique=True, verbose_name='URL')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Phone, self).save(*args, **kwargs)

    def __str__(self):
        return self.slug

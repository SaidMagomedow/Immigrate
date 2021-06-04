from django.db import models

# Create your models here.
from django.urls import reverse

from Sham.accounts.models import CreatedByModel, TimeStampedModel
from Sham.accounts.validators import validate_image_extension


class Article(CreatedByModel, TimeStampedModel):

    CATEGORY_CHOISES = {
        (IMMIGRATE := 'IMMIGRATE', 'Переезд'),
        (SIGHT := 'SIGHT', 'Достпримечательности'),
        (CRITICISM := 'CRITICISM', 'Критика'),
    }

    title = models.CharField('Заголовок статьи', max_length=155, unique=True)
    category = models.CharField('Категория статьи', max_length=25, choices=CATEGORY_CHOISES)
    file = models.FileField('Файл', validators=[validate_image_extension])
    description = models.CharField('Описание', max_length=255)
    some_article = models.CharField('Статья', max_length=1000)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def get_absolute_url(self):
        return reverse('content:article-detail', kwargs={'pk': self.pk})


class Country(CreatedByModel, TimeStampedModel):

    PART_TYPES = (
        (EUROPE := 'EUROPE', 'Европа'),
        (AFRICA := 'AFRICA', 'Африка'),
        (ASIA := 'ASIA', 'Азия'),
        (SOUTH_AMERICA := 'SOUTH_AMERICA', 'Южная Америка'),
        (NORTH_AMERICA := 'NORTH_AMERICA', 'Северная Америка'),
        (AUSTRALIA := 'AUSTRALIA', 'Австралия'),
    )

    country = models.ForeignKey(Article, on_delete=models.DO_NOTHING, verbose_name="Страна")
    part_world = models.CharField('Часть света',choices=PART_TYPES, max_length=155)

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'

    def get_absolute_url(self):
        return reverse('content:county-detail', kwargs={'pk': self.pk})
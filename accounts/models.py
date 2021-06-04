from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.db import models
from django.urls import reverse
from django_currentuser.db.models import CurrentUserField
# Create your models here.


class Mixin:
    def get_name(self):
        return ' '.join(filter(None, [self.name]))  # noqa

    def get_email(self):
        return self.email # noqa


class CreatedAtModel(models.Model):
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        abstract = True


class CreatedByModel(models.Model):
    created_by = CurrentUserField(verbose_name='Пользователь')

    class Meta:
        abstract = True


class UpdatedAtModel(models.Model):
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)

    class Meta:
        abstract = True


class TimeStampedModel(CreatedAtModel, UpdatedAtModel):
    class Meta:
        abstract = True


class User(Mixin, AbstractBaseUser, PermissionsMixin):
    STATUSES = (
        (MODERATOR := 'MODERATOR', 'Модератор'),
        (ARTICLES_AUTHOR := 'ARTICLES_AUTHOR', 'Автор статей'),
        (READER := 'READER', 'Читатель'),
    )

    country = models.CharField('страна', max_length=25)
    email = models.EmailField('email', unique=True)
    name = models.CharField('Имя пользователя', max_length=255)
    status = models.CharField('Статус пользователя', max_length=10, choices=STATUSES, default=READER)
    articles = models.ForeignKey('content.Article', on_delete=models.DO_NOTHING, verbose_name='Автор статьи')

    objects = UserManager()

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def get_absolute_url(self):
        return reverse('accounts:staff-detail', kwargs={'pk': self.pk})

    def is_modetator(self):
        return self.status == User.MODERATOR

    def is_author(self):
        return self.status == User.ARTICLES_AUTHOR

    def is_reader(self):
        return self.status == User.READER
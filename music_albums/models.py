#coding:utf-8

# Django imports
import django.db.models
import datetime

# Music Albums imports
import common

class Album(django.db.models.Model):

    RATING_CHOICES = (
        (1, "★"),
        (2, "★★"),
        (3, "★★★"),
        (4, "★★★★"),
        (5, "★★★★★")
    )

    title = django.db.models.CharField(
        verbose_name=common.MODEL_FIELD__TITLE
    )
    release_date = django.db.models.DateTimeField(
        verbose_name=common.MODEL_FIELD__RELEASE_DATE,
        blank=True
    )
    rating = django.db.models.IntegerField(
        choices=RATING_CHOICES,
        verbose_name=common.MODEL_FIELD__RATING,
        blank=True
    )
    cover = django.db.models.ImageField(
        upload_to="images/albums",
        verbose_name=common.MODEL_FIELD__COVER,
        default="images/albums/default.jpg"
    )
    label = django.db.models.ForeignKey(
        Label,
        on_delete=django.db.models.PROTECT,
        related_name="album",
        verbose_name=common.MODEL_NAME__RECORD_LABEL,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = common.MODEL_NAME__ALBUM
        verbose_name_plural = common.MODEL_NAME__ALBUM_PLURAL

    def __str__(self):
        return self.title


class Artist(django.db.models.Model):

    name = django.db.models.CharField(
        verbose_name=common.MODEL_FIELD__NAME
    )
    albums = django.db.models.ManyToManyField(
        Album,
        related_name="artists",
        verbose_name=common.MODEL_NAME__ALBUM_PLURAL
    )

    class Meta:
        verbose_name = common.MODEL_NAME__ARTIST
        verbose_name_plural = common.MODEL_NAME__ARTIST_PLURAL

    def __str__(self):
        return self.name


class Label(django.db.models.Model):

    name = django.db.models.CharField(
        verbose_name=common.MODEL_FIELD__NAME
    )
    is_operating = django.db.models.BooleanField(
        verbose_name=common.MODEL_FIELD__IS_OPERATING,
        default=True
    )

    class Meta:
        verbose_name = common.MODEL_NAME__RECORD_LABEL
        verbose_name_plural = common.MODEL_NAME__RECORD_LABEL_PLURAL

    def __str__(self):
        return self.name
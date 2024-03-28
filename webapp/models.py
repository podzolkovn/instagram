from django.db import models
from django.contrib.auth import get_user_model


class Public(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        related_name="public_users",
        verbose_name='user',
        on_delete=models.CASCADE
    )
    description = models.TextField(
        max_length=3000,
        null=False,
        verbose_name='description'
    )
    img_files = models.ImageField(
        verbose_name='media',
        upload_to='avatars'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='data_at',
    )


class Like(models.Model):
    public = models.ForeignKey(
        'Public',
        verbose_name='public',
        related_name='like_public',
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        get_user_model(),
        related_name="like_users",
        verbose_name='user',
        on_delete=models.DO_NOTHING
    )


class Comment(models.Model):
    comment = models.TextField(
        max_length=3000,
        null=False,
        verbose_name='comment'
    )
    public = models.ForeignKey(
        'Public',
        verbose_name='public',
        related_name='comment_public',
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        get_user_model(),
        related_name="comment_user",
        verbose_name='user',
        on_delete=models.DO_NOTHING
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='data at'
    )

from django.db import models

from user.models import User


class Article(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'article'
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
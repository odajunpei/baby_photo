from django.db import models

# Create your models here.


class Baby(models.Model):
    title = models.CharField(verbose_name="タイトル", max_length=200)
    content = models.TextField(verbose_name="内容")

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "ベイビー"
        verbose_name_plural = "ベイビー"

    def __str__(self):
      return self.title

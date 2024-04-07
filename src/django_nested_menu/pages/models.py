from django.db import models


class Page(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.SlugField(unique=True)
    path = models.CharField(max_length=100, unique=True)
    parent = models.ForeignKey(
        'self', blank=True, null=True,
        on_delete=models.CASCADE, related_name='children'
    )

    def __str__(self):
        return self.title

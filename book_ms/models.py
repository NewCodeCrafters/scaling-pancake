from django.db import models
from django.utils.text import slugify


STATUS = (
    ("published","published"),
    ("unpublished","unpublished")
)

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=220, blank=True)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Categories"
        verbose_name = "Category"


class Book(models.Model):
    name = models.CharField(max_length=120)
    author = models.CharField(max_length=50)
    category = models.ManyToManyField(Category)
    Documents = models.FileField()
    cover_image = models.ImageField(upload_to="media")
    status = models.CharField(max_length=100, choices=STATUS)
    pages = models.IntegerField(default=0)

    

class Comments(models.Model):
    comment = models.TextField()
    likes = models.IntegerField()


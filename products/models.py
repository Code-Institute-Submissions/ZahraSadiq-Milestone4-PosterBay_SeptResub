from django.db import models

# Create your models here.


class Categories(models.Model):

    class Meta:
        verbose_name_plural = 'Category'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(
        max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    categories = models.ForeignKey(
        "Categories", null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(
        max_length=250, null=True, blank=True)
    name = models.CharField(max_length=300)
    description = models.TextField()
    side_note = models.TextField()
    artist = models.CharField(max_length=250)
    artist_id = models.CharField(max_length=100, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(
        max_length=2000, null=True, blank=True)
    image = models.ImageField(
        null=True, blank=True)

    def __str__(self):
        return self.name

from django.db import models
from category.models import Category
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    CHOICES=(
        ('0','Not Available'),
        ('1','Available'),
    )
    product_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=500, blank=True)
    price = models.IntegerField()
    images = models.ImageField(upload_to='photos/store')
    stock = models.IntegerField()
    is_available = models.BooleanField(choices=CHOICES, default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.product_name)
        super(Product, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('product-detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_name
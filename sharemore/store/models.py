from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    
    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.title
    
class Item(models.Model):
    user = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    description = models.TextField(blank=True)
    value = models.IntegerField()
    image = models.ImageField(upload_to='uploads/item_images/', blank=True, null=True)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    is_deleted = models.BooleanField(default=False)
    
    class Meta:
        ordering = ('-created_date',)
    
    def __str__(self):
        return self.title
    
    def get_display_value(self):
        return self.value / 100
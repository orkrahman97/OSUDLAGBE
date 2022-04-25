from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Categories"

class Product(models.Model):
    main_image = models.ImageField(upload_to='products')
    name = models.CharField(max_length=264)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="category")
    preview_text = models.TextField(max_length=200,verbose_name="preview_text")
    detail_text = models.TextField(max_length=1000,verbose_name="description")
    price = models.FloatField(default=0.00)
    old_price = models.FloatField(default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-created_at',]
        verbose_name_plural = "Products"
        
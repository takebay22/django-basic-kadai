from django.db import models
from django.urls import reverse

# Categoryクラスの定義
class Category(models.Model):
    name = models.CharField(max_length=200)
 
    def __str__(self):
        return self.name

# Productクラスの定義
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    img = models.ImageField(blank=True, default='noImage.png')

    def __str__(self):
        return self.name

    # 新規作成・編集完了時のリダイレクト先
    def get_absolute_url(self):
        return reverse('list')

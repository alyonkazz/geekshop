from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(verbose_name='имя категории',
                            max_length=128,
                            unique=True)
    description = models.TextField(verbose_name='описание',
                                   blank=True)
    is_active = models.BooleanField(verbose_name='активность', default=True)

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='имя продукта', max_length=128)
    image = models.ImageField(upload_to='products_image', blank=True)
    short_desc = models.CharField(verbose_name='короткое описание продукта', max_length=60, blank=True)
    description = models.TextField(verbose_name='описание продукта', blank=True)
    price = models.DecimalField(verbose_name='цена продукта', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='количество на складе', default=0)
    is_active = models.BooleanField(verbose_name='активность', default=True)

    def __str__(self):
        return f"{self.name} ({self.category.name})"

    @staticmethod
    def get_items():
        return Product.objects.filter(is_active=True).order_by('category', 'name')

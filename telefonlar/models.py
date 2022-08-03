from django.db import models

class Brand(models.Model):
    brand_id = models.AutoField(primary_key=True)
    brand_name = models.TextField()

    class Meta:
        verbose_name_plural = 'Brandlar'

    def __str__(self):
        return self.brand_name

class Madel(models.Model):
    madel_id = models.AutoField(primary_key=True)
    madel_name = models.TextField()
    brand = models.ForeignKey('Brand', models.DO_NOTHING)

    class Meta:
        verbose_name_plural = 'Madellar'

    def __str__(self):
        return self.madel_name

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_title = models.TextField()
    product_description = models.TextField()
    product_brand = models.ForeignKey('Brand', models.DO_NOTHING)
    product_madel = models.ForeignKey('Madel', models.DO_NOTHING)
    product_price = models.IntegerField()
    product_color = models.TextField()
    product_memory = models.TextField()

    class Meta:
        verbose_name_plural = 'Produktlar'

    def __str__(self):
        return self.product_title
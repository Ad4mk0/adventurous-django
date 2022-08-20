from django.db import models

## All the models ##


class AttributeName(models.Model):
    _id = models.AutoField(primary_key=True)
    id = models.IntegerField(unique=False)
    nazev = models.CharField(blank=True, max_length=300)
    zobrazit = models.BooleanField(blank=True, null=True)
    kod = models.CharField(blank=True, max_length=300)


class AttributeValue(models.Model):
    _id = models.AutoField(primary_key=True)
    id = models.IntegerField(unique=False)
    hodnota = models.CharField(max_length=300)


class Attribute(models.Model):
    _id = models.AutoField(primary_key=True)
    id = models.IntegerField(unique=False)
    nazev_atributu_id = models.IntegerField()
    hodnota_atributu_id = models.IntegerField()


class Product(models.Model):
    _id = models.AutoField(primary_key=True)
    id = models.IntegerField(unique=False)
    nazev = models.CharField(blank=True, max_length=300)
    description = models.CharField(blank=True, max_length=500)
    cena = models.CharField(max_length=15)
    mena = models.CharField(blank=True, max_length=30)
    published_on = models.DateTimeField(null=True, blank=True)
    is_published = models.BooleanField(blank=True, null=True)


class Image(models.Model):
    _id = models.AutoField(primary_key=True)
    id = models.IntegerField(unique=False)
    nazev = models.CharField(blank=True, max_length=300)
    obrazek = models.CharField(max_length=300)


class Catalog(models.Model):
    _id = models.AutoField(primary_key=True)
    id = models.IntegerField(unique=False)
    nazev = models.CharField(blank=True, max_length=300)
    obrazek_id = models.IntegerField(null=True, blank=True)
    products_ids = models.JSONField(default=dict)
    attributes_ids = models.JSONField(default=dict)


class ProductImage(models.Model):
    _id = models.AutoField(primary_key=True)
    id = models.IntegerField(unique=False)
    product = models.IntegerField()
    obrazek_id = models.IntegerField()
    nazev = models.CharField(max_length=300)


class ProductAttributes(models.Model):
    _id = models.AutoField(primary_key=True)
    id = models.IntegerField(unique=False)
    attribute = models.IntegerField()
    product = models.IntegerField()

# Generated by Django 4.1 on 2022-08-20 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whys', '0002_attribute_attributename_attributevalue_catalog_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalog',
            name='attributes_ids',
            field=models.JSONField(default=[]),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='products_ids',
            field=models.JSONField(default=[]),
        ),
    ]
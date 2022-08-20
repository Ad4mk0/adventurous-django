# Generated by Django 4.1 on 2022-08-20 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whys', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('id', models.IntegerField()),
                ('nazev_atributu_id', models.IntegerField()),
                ('hodnota_atributu_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='AttributeName',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('id', models.IntegerField()),
                ('nazev', models.CharField(blank=True, max_length=300)),
                ('zobrazit', models.BooleanField(blank=True, null=True)),
                ('kod', models.CharField(blank=True, max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='AttributeValue',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('id', models.IntegerField()),
                ('hodnota', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('id', models.IntegerField()),
                ('nazev', models.CharField(blank=True, max_length=300)),
                ('obrazek_id', models.IntegerField(blank=True, null=True)),
                ('products_ids', models.JSONField(default={})),
                ('attributes_ids', models.JSONField(default={})),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('id', models.IntegerField()),
                ('nazev', models.CharField(blank=True, max_length=300)),
                ('obrazek', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('id', models.IntegerField()),
                ('nazev', models.CharField(blank=True, max_length=300)),
                ('description', models.CharField(blank=True, max_length=500)),
                ('cena', models.CharField(max_length=15)),
                ('mena', models.CharField(blank=True, max_length=30)),
                ('published_on', models.DateTimeField(blank=True, null=True)),
                ('is_published', models.BooleanField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductAttributes',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('id', models.IntegerField()),
                ('attribute', models.IntegerField()),
                ('product', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('id', models.IntegerField()),
                ('product', models.IntegerField()),
                ('obrazek_id', models.IntegerField()),
                ('nazev', models.CharField(max_length=300)),
            ],
        ),
        migrations.DeleteModel(
            name='Drink',
        ),
    ]

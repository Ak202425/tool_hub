# Generated by Django 4.2.11 on 2024-04-30 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toolhub', '0002_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='static'),
        ),
    ]

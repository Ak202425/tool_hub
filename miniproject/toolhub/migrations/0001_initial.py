# Generated by Django 4.2.11 on 2024-04-30 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(upload_to='static/images')),
                ('category', models.CharField(choices=[('air compressor', 'Air Compressor'), ('power_tools_and_accessories', 'Power Tools and Accessories'), ('machine_tools', 'Machine Tools')], max_length=100)),
            ],
        ),
    ]
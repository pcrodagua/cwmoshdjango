# Generated by Django 5.0.1 on 2024-01-27 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_rename_last_updated_product_last_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='-', max_length=255),
        ),
    ]

# Generated by Django 5.0.1 on 2024-01-27 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_address_zipcode_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collection',
            old_name='feature_product',
            new_name='featured_product',
        ),
    ]

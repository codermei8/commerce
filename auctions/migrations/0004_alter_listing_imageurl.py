# Generated by Django 4.1.5 on 2023-01-25 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_alter_listing_category_alter_listing_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='imageURL',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]

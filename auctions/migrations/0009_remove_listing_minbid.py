# Generated by Django 4.1.5 on 2023-01-26 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_listing_minbid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='minBid',
        ),
    ]

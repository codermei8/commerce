# Generated by Django 4.1.5 on 2023-01-26 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_bid_bid_bid_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='minBid',
            field=models.FloatField(default=0),
        ),
    ]

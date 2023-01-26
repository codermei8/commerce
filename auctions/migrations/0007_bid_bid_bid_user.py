# Generated by Django 4.1.5 on 2023-01-26 12:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_comment_author_comment_listing_comment_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='bid',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='bid',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userBid', to=settings.AUTH_USER_MODEL),
        ),
    ]

# Generated by Django 3.1.6 on 2021-03-05 16:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0007_ses_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='poll',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

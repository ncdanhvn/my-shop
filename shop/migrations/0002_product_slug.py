# Generated by Django 4.2.5 on 2023-09-09 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.CharField(default=' ', max_length=255),
            preserve_default=False,
        ),
    ]
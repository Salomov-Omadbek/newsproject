# Generated by Django 4.0 on 2024-02-02 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0005_alter_news_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='image',
            new_name='images',
        ),
    ]

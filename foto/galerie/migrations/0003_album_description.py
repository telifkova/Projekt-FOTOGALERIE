# Generated by Django 4.2.9 on 2024-02-20 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galerie', '0002_album_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='description',
            field=models.TextField(null=True),
        ),
    ]

# Generated by Django 4.2.6 on 2023-11-06 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_autor_post_author_rename_creado_post_created_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
    ]

# Generated by Django 4.2.6 on 2023-11-05 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='autor',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='creado',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='contenido',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='titulo',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='actualizado',
            new_name='updated',
        ),
    ]
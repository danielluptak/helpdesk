# Generated by Django 4.0.1 on 2022-02-26 23:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0005_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment_author',
            new_name='author',
        ),
    ]

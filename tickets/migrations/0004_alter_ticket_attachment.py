# Generated by Django 4.0.1 on 2022-02-25 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0003_ticket_attachment_alter_ticket_it_assigned'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to='images'),
        ),
    ]

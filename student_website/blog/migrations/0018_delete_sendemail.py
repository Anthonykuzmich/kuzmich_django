# Generated by Django 3.1.4 on 2020-12-25 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_sendemail'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SendEmail',
        ),
    ]
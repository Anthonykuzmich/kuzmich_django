# Generated by Django 3.1.4 on 2020-12-24 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20201224_0753'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='shere',
            new_name='sphere',
        ),
    ]
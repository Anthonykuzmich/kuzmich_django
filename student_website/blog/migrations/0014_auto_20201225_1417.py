# Generated by Django 3.1.4 on 2020-12-25 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_post_header_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='header_image',
            new_name='image',
        ),
    ]
# Generated by Django 3.1.4 on 2020-12-21 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='speciality',
        ),
        migrations.RemoveField(
            model_name='post',
            name='body',
        ),
    ]
# Generated by Django 3.1.3 on 2020-12-06 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cw22', '0003_diary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diary',
            name='student',
        ),
        migrations.AddField(
            model_name='person',
            name='gpa',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cw22.diary'),
        ),
    ]

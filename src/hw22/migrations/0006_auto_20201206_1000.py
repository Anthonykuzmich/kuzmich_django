# Generated by Django 3.1.3 on 2020-12-06 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hw22', '0005_auto_20201206_0953'),
    ]

    operations = [
        migrations.AddField(
            model_name='musicband',
            name='album',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hw22.album'),
        ),
        migrations.AlterField(
            model_name='album',
            name='band',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bands', to='hw22.musicband'),
        ),
        migrations.AlterField(
            model_name='track',
            name='album',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='albums', to='hw22.album'),
        ),
    ]

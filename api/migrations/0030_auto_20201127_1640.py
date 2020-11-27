# Generated by Django 3.0.8 on 2020-11-27 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0029_auto_20201113_2018'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='extension',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='file',
            name='song',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='files', to='api.Song'),
        ),
    ]

# Generated by Django 4.0.8 on 2023-07-18 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swingtime', '0002_alter_occurrence_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.CharField(blank=True, max_length=1000, verbose_name='description'),
        ),
    ]

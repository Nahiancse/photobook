# Generated by Django 3.1.5 on 2021-01-31 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0006_auto_20210130_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photobook',
            name='published_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]

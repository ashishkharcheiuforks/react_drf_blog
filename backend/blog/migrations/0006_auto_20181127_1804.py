# Generated by Django 2.1.3 on 2018-11-27 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20180613_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='title',
            field=models.CharField(db_index=True, max_length=100),
        ),
    ]

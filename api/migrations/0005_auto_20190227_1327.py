# Generated by Django 2.1.7 on 2019-02-27 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20190227_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='element',
            name='date',
            field=models.DateField(auto_now_add=True, verbose_name='дата'),
        ),
    ]

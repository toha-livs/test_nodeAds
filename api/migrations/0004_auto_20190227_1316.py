# Generated by Django 2.1.7 on 2019-02-27 13:16

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20190227_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='element',
            name='icon',
            field=models.ImageField(upload_to='static/icon/element/', validators=[api.models.validator_icon], verbose_name='иконка'),
        ),
    ]
# Generated by Django 2.1.7 on 2019-02-26 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('icon', models.ImageField(upload_to='media/icon/')),
                ('name', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=512)),
            ],
        ),
    ]
# Generated by Django 2.2.1 on 2021-01-25 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0005_auto_20210125_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='headimg',
            field=models.ImageField(default='1.jpg', upload_to='seller/img'),
        ),
    ]
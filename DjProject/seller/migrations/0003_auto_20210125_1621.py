# Generated by Django 2.2.1 on 2021-01-25 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0002_auto_20210125_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='logo',
            field=models.ImageField(default='1.jpg', upload_to='seller/img'),
        ),
    ]
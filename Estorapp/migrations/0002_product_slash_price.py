# Generated by Django 4.2 on 2023-04-12 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Estorapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slash_price',
            field=models.FloatField(null=True),
        ),
    ]

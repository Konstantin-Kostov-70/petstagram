# Generated by Django 4.1.1 on 2022-10-11 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0003_pet_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='name',
            field=models.CharField(max_length=31),
        ),
    ]

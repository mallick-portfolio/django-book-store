# Generated by Django 5.0 on 2023-12-30 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_category_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='book category'),
        ),
    ]

# Generated by Django 5.0 on 2023-12-30 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_userbankaccount_balance_after_borrow'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userbankaccount',
            name='balance_after_borrow',
        ),
    ]

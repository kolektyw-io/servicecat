# Generated by Django 3.2 on 2021-06-15 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commons', '0003_auto_20210615_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='mnemonic',
            field=models.CharField(default='', max_length=50),
        ),
    ]

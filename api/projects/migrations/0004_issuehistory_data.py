# Generated by Django 3.2.7 on 2021-09-30 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20210930_1046'),
    ]

    operations = [
        migrations.AddField(
            model_name='issuehistory',
            name='data',
            field=models.CharField(default='{}', max_length=8192),
            preserve_default=False,
        ),
    ]

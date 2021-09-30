# Generated by Django 3.2.7 on 2021-09-30 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_issuehistory_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuestate',
            name='as_done',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='issuestate',
            name='as_draft',
            field=models.BooleanField(default=True),
        ),
    ]
# Generated by Django 3.2.7 on 2021-09-30 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20210930_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issueschema',
            name='workflow',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='projects.workflow'),
        ),
    ]

# Generated by Django 3.1 on 2020-10-09 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_ttestcasestepresult_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tinterfacemain',
            name='pid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.tproject'),
        ),
    ]
# Generated by Django 4.0.6 on 2022-07-29 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_user', '0005_alter_mainuser_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainuser',
            name='first_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
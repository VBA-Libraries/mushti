# Generated by Django 4.0.6 on 2022-07-29 08:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project_contribution', '0002_rename_projectconstribution_projectcontribution'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectcontribution',
            name='contributor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

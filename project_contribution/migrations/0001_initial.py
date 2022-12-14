# Generated by Django 4.0.6 on 2022-07-28 05:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contributor', '0001_initial'),
        ('project', '0002_project_project_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectConstribution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=16)),
                ('contribution_date', models.DateTimeField(auto_now_add=True)),
                ('comments', models.TextField()),
                ('contributor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contributor.contributor')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.project')),
            ],
        ),
    ]

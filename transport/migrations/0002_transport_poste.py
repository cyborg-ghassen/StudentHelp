# Generated by Django 5.0.3 on 2024-03-30 20:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_reaction'),
        ('transport', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transport',
            name='poste',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='post.post'),
            preserve_default=False,
        ),
    ]

# Generated by Django 5.0.3 on 2024-03-30 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='poste/%Y/%m/%d')),
                ('type', models.CharField(choices=[('0', 'Offre'), ('1', 'Demande')], max_length=80)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
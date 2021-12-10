# Generated by Django 4.0 on 2021-12-09 09:15

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='carousel/', verbose_name='Carousel Image')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('description', models.CharField(max_length=500, verbose_name='Description')),
                ('enabled', models.BooleanField(default=True, verbose_name='Enabled')),
            ],
            options={
                'verbose_name': 'Carousel',
            },
        ),
        migrations.CreateModel(
            name='SiteLogo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=15, verbose_name='Site Title')),
                ('logo', models.FileField(upload_to='main/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['svg', 'png', 'jpg'])], verbose_name='Site Logo')),
            ],
            options={
                'verbose_name': 'Site Logo',
            },
        ),
        migrations.CreateModel(
            name='CarouselAction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=10, verbose_name='Label')),
                ('button', models.CharField(choices=[('danger', 'Red'), ('primary', 'Blue'), ('warning', 'Yellow'), ('dark ', 'Dark')], default='primary', max_length=20, verbose_name='Button')),
                ('action', models.URLField(verbose_name='Action')),
                ('outline', models.BooleanField(default=True, verbose_name='Outline')),
                ('enabled', models.BooleanField(default=True, verbose_name='Enabled')),
                ('carousel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.carousel')),
            ],
            options={
                'verbose_name': 'Carousel Action',
            },
        ),
    ]

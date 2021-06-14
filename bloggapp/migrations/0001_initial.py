# Generated by Django 3.2.2 on 2021-05-27 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('slug', models.SlugField()),
                ('description', models.TextField()),
                ('name', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField()),
            ],
        ),
    ]

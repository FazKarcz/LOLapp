# Generated by Django 4.2.9 on 2024-01-10 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=25)),
                ('title', models.CharField(max_length=35)),
                ('date', models.DateField(auto_now=True)),
                ('text', models.TextField(max_length=1500)),
            ],
        ),
    ]

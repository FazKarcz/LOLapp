# Generated by Django 4.2.9 on 2024-01-03 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=256, unique=True)),
                ('description', models.TextField(max_length=500)),
                ('item_price', models.IntegerField()),
                ('is_mythic', models.BooleanField()),
            ],
        ),
    ]

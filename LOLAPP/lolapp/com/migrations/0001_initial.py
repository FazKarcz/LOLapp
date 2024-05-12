# Generated by Django 4.2.9 on 2024-01-14 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=25)),
                ('content', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='com', to='news.news')),
            ],
        ),
    ]
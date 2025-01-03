# Generated by Django 4.2 on 2024-12-28 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RadioStation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('call_sign', models.CharField(max_length=10)),
                ('slogan', models.CharField(max_length=200)),
                ('streaming_url', models.URLField()),
                ('image', models.ImageField(upload_to='radio_image/')),
            ],
        ),
    ]

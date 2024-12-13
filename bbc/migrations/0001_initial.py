# Generated by Django 5.1.2 on 2024-12-13 17:32

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
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('views', models.IntegerField(default=0)),
                ('is_published', models.BooleanField(default=False)),
            ],
        ),
    ]

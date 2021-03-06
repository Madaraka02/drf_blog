# Generated by Django 4.0.6 on 2022-07-13 10:12

import autoslug.fields
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
                ('title', models.CharField(max_length=400, null=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title')),
                ('image', models.FileField(upload_to='blogs')),
                ('description', models.TextField(null=True)),
                ('snippet', models.CharField(max_length=400, null=True)),
            ],
        ),
    ]

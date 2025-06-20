# Generated by Django 5.0.12 on 2025-06-09 05:55

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0005_enquiry'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('image', models.ImageField(upload_to='trip/')),
                ('title', models.CharField(max_length=255)),
                ('place_name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Trip-Highlights',
            },
        ),
    ]

# Generated by Django 5.0.12 on 2025-06-08 14:48

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0003_collegepartners'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndustryPartners',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('image', models.ImageField(upload_to='industry/')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('hq', models.CharField(max_length=255)),
                ('highlight', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Industry-Partners',
            },
        ),
    ]

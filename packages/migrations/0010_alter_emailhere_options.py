# Generated by Django 5.0.12 on 2025-06-09 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0009_emailhere_alter_blog_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='emailhere',
            options={'verbose_name_plural': 'User-Email'},
        ),
    ]

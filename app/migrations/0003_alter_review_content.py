# Generated by Django 4.2.5 on 2023-09-21 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_review_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='content',
            field=models.TextField(verbose_name='Текст'),
        ),
    ]

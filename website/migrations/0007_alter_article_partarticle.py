# Generated by Django 5.0.2 on 2024-03-28 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='partArticle',
            field=models.TextField(blank=True),
        ),
    ]
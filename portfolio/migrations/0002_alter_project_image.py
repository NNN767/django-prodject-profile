# Generated by Django 5.0.2 on 2024-02-14 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(max_length=50, upload_to='portfolio/images/'),
        ),
    ]
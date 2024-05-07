# Generated by Django 5.0.2 on 2024-05-07 09:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tags',
            new_name='Tag',
        ),
        migrations.AlterField(
            model_name='blog',
            name='cover_image',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='blog_cover_image', to='blog.coverimage'),
        ),
    ]
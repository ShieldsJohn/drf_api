# Generated by Django 5.0.7 on 2024-07-21 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profile_image_alter_profile_content'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='content',
            new_name='bio',
        ),
        migrations.AddField(
            model_name='profile',
            name='social_media_link1',
            field=models.URLField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='profile',
            name='social_media_link2',
            field=models.URLField(blank=True, max_length=255),
        ),
    ]

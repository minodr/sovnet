# Generated by Django 5.0.4 on 2024-04-22 12:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="bio",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="first_name",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="last_name",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="profile_picture",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="public_key",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
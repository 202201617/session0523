# Generated by Django 5.0.6 on 2024-06-02 06:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("coplate", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="first_name",
            field=models.CharField(
                blank=True, max_length=150, verbose_name="first name"
            ),
        ),
    ]

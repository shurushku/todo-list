# Generated by Django 4.1.3 on 2022-11-14 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("todo", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="task",
            options={"ordering": ["done", "-datetime"]},
        ),
    ]

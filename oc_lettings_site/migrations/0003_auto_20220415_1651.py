# Generated by Django 3.0 on 2022-04-15 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("oc_lettings_site", "0002_auto_20220415_1618"),
        ("profiles", "0002_auto_20220415_1619"),
        ("lettings", "0003_auto_20220415_1635"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Address",
        ),
        migrations.RemoveField(
            model_name="profile",
            name="user",
        ),
        migrations.DeleteModel(
            name="Letting",
        ),
        migrations.DeleteModel(
            name="Profile",
        ),
    ]

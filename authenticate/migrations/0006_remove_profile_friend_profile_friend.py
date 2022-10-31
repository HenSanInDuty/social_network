# Generated by Django 4.1.2 on 2022-10-31 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authenticate", "0005_merge_20221031_0934"),
    ]

    operations = [
        migrations.RemoveField(model_name="profile", name="friend",),
        migrations.AddField(
            model_name="profile",
            name="friend",
            field=models.ManyToManyField(
                blank=True, null=True, to="authenticate.profile"
            ),
        ),
    ]

# Generated by Django 4.2.3 on 2023-07-25 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("aplikasi_maspix", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="blog", name="date",),
        migrations.AddField(
            model_name="blog",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="blog/"),
        ),
    ]

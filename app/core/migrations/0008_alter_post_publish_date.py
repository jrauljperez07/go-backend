# Generated by Django 3.2.16 on 2022-11-13 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_post_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

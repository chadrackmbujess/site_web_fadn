# Generated by Django 5.0.4 on 2024-07-13 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0022_alter_profile_profile_photo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Internship',
        ),
        migrations.AddField(
            model_name='profile',
            name='desc',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]

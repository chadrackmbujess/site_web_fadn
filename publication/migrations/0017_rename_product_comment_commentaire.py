# Generated by Django 5.0.4 on 2024-07-11 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0016_rename_comment_comment_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='product',
            new_name='commentaire',
        ),
    ]

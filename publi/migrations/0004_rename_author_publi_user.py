# Generated by Django 4.1.7 on 2023-05-29 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publi', '0003_rename_user_publi_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publi',
            old_name='author',
            new_name='user',
        ),
    ]

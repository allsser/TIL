# Generated by Django 2.2.6 on 2019-11-04 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_comment_article'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='updated_ad',
            new_name='updated_at',
        ),
    ]

# Generated by Django 3.2.16 on 2023-03-12 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_alter_post_group'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='unique subscription',
        ),
    ]
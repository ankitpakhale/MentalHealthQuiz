# Generated by Django 3.0 on 2022-04-03 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20220403_1408'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signupform',
            name='marks',
        ),
    ]
# Generated by Django 2.1.5 on 2019-04-12 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjective', '0010_auto_20190412_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answersub',
            name='user_ans',
            field=models.CharField(max_length=2000, verbose_name='userbyans'),
        ),
        migrations.AlterField(
            model_name='subscore',
            name='usersub',
            field=models.CharField(max_length=2000, verbose_name='usersub'),
        ),
    ]

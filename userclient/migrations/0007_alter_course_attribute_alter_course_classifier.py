# Generated by Django 5.0.2 on 2024-02-25 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userclient', '0006_remove_superadmin_author_delete_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='attribute',
            field=models.SmallIntegerField(verbose_name='课程属性'),
        ),
        migrations.AlterField(
            model_name='course',
            name='classifier',
            field=models.CharField(max_length=1, verbose_name='课程类别'),
        ),
    ]

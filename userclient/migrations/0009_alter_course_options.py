# Generated by Django 5.0.2 on 2024-02-25 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userclient', '0008_alter_course_options_alter_department_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name': '课程库', 'verbose_name_plural': '课程库'},
        ),
    ]

# Generated by Django 4.2.13 on 2024-07-25 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_remove_staffmember_image_staffmember_staff_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffmember',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='staffmember',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='staffmember',
            name='role',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
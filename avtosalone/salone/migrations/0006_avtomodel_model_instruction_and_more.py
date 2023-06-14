# Generated by Django 4.2 on 2023-06-01 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salone', '0005_rename_sevice_customer_comment_serviceregistration_service_customer_comment_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='avtomodel',
            name='model_instruction',
            field=models.FileField(blank=True, upload_to='book/'),
        ),
        migrations.AlterField(
            model_name='avtomodel',
            name='model_ph_1',
            field=models.ImageField(upload_to='image/'),
        ),
        migrations.AlterField(
            model_name='avtomodel',
            name='model_ph_2',
            field=models.ImageField(upload_to='image/'),
        ),
        migrations.AlterField(
            model_name='avtomodel',
            name='model_ph_3',
            field=models.ImageField(upload_to='image/'),
        ),
        migrations.AlterField(
            model_name='serviceregistration',
            name='service_date',
            field=models.DateField(),
        ),
    ]

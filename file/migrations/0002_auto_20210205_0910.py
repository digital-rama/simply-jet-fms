# Generated by Django 3.1.6 on 2021-02-05 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadedfile',
            name='md5_hash',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name=''),
        ),
    ]
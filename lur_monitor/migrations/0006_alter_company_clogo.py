# Generated by Django 4.2.5 on 2023-12-20 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lur_monitor', '0005_alter_company_clogo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='cLogo',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]

# Generated by Django 4.2.4 on 2023-08-17 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_alter_candidato_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidato',
            name='foto',
            field=models.ImageField(null=True, upload_to='images/', verbose_name='Image'),
        ),
    ]

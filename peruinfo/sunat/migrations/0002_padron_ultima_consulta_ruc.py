# Generated by Django 4.2.3 on 2023-08-23 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sunat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='padron',
            name='ultima_consulta_ruc',
            field=models.DateField(blank=True, null=True),
        ),
    ]

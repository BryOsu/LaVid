# Generated by Django 5.0.6 on 2024-08-02 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_cliente_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='bodegas',
            name='anio',
            field=models.CharField(default=1, max_length=4),
            preserve_default=False,
        ),
    ]

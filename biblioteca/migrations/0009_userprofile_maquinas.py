# Generated by Django 4.2.3 on 2023-11-09 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0008_maquina_tipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='maquinas',
            field=models.ManyToManyField(blank=True, related_name='usuarios', to='biblioteca.maquina'),
        ),
    ]

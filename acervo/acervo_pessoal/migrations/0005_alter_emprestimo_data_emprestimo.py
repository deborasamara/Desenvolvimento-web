# Generated by Django 5.1.1 on 2024-09-15 17:03

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acervo_pessoal', '0004_alter_contato_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='data_emprestimo',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

# Generated by Django 5.1.1 on 2024-09-15 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acervo_pessoal', '0003_contato_usuario_alter_contato_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='email',
            field=models.EmailField(max_length=255),
        ),
    ]
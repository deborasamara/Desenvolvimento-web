# Generated by Django 5.1.1 on 2024-09-14 02:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('autor', models.CharField(max_length=255)),
                ('ano', models.IntegerField()),
                ('foto', models.ImageField(upload_to='capas/')),
            ],
        ),
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_emprestimo', models.DateTimeField()),
                ('data_devolucao', models.DateTimeField(blank=True, null=True)),
                ('status_emprestimo', models.CharField(choices=[('ativo', 'Ativo'), ('devolvido', 'Devolvido')], default='ativo', max_length=10)),
                ('contato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acervo_pessoal.contato')),
                ('usuario_portador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('livro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acervo_pessoal.livro')),
            ],
        ),
    ]
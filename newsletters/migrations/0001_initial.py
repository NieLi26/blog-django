# Generated by Django 3.2.6 on 2022-07-25 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsletterUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Correo')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
            ],
            options={
                'verbose_name': 'NewsletterUser',
                'verbose_name_plural': 'NewsletterUsers',
            },
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Nombre')),
                ('subject', models.CharField(max_length=250, verbose_name='Asunto')),
                ('body', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('email', models.ManyToManyField(to='newsletters.NewsletterUser')),
            ],
            options={
                'verbose_name': 'Newsletter',
                'verbose_name_plural': 'Newsletters',
            },
        ),
    ]

# Generated by Django 4.1.1 on 2022-10-15 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='subirHistoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=40)),
                ('nombreCreador', models.CharField(max_length=40)),
                ('cuerpoHistoria', models.CharField(max_length=9999)),
                ('fechaHistoria', models.DateField()),
            ],
        ),
    ]

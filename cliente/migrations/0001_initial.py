# Generated by Django 2.0 on 2018-06-25 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_register', models.DateTimeField(auto_now=True)),
                ('nome', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('cidade', models.CharField(max_length=200)),
                ('bairro', models.CharField(max_length=200)),
                ('telefone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='FipeDetail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('marca', models.CharField(max_length=200)),
                ('modelo', models.CharField(max_length=200)),
                ('ano', models.IntegerField()),
                ('valor', models.CharField(max_length=200)),
                ('dd_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SeguroDetail',
            fields=[
                ('fipe_detail', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='cliente.FipeDetail')),
            ],
        ),
        migrations.AddField(
            model_name='fipedetail',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cliente.Cliente'),
        ),
    ]

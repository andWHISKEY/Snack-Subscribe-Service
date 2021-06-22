# Generated by Django 3.1.2 on 2020-10-17 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Snack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('describe', models.CharField(max_length=500)),
                ('summary', models.CharField(max_length=300)),
                ('image', models.ImageField(null=True, upload_to='images/')),
                ('with_who', models.CharField(max_length=20)),
                ('texture', models.CharField(max_length=20)),
                ('flavor', models.CharField(max_length=20)),
                ('situation', models.CharField(max_length=20)),
            ],
        ),
    ]
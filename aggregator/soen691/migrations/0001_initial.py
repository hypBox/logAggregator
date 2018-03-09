# Generated by Django 2.0.3 on 2018-03-09 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_local', models.CharField(max_length=200)),
                ('remote_addr', models.CharField(max_length=200)),
                ('request', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=50)),
                ('req_time', models.CharField(max_length=50)),
                ('http_user_agent', models.CharField(max_length=500)),
            ],
        ),
    ]

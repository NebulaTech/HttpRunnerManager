# Generated by Django 2.0 on 2017-12-30 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ApiManager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestCaseInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_name', models.CharField(max_length=50)),
                ('belong_project', models.CharField(max_length=50)),
                ('include', models.CharField(max_length=200, null=True)),
                ('author', models.CharField(max_length=20)),
                ('variables', models.TextField(null=True)),
                ('url', models.CharField(max_length=30)),
                ('method', models.CharField(max_length=10)),
                ('data_type', models.CharField(max_length=10)),
                ('request', models.TextField(null=True)),
                ('headers', models.TextField(null=True)),
                ('extract', models.TextField()),
                ('validate', models.TextField()),
                ('status', models.IntegerField(default=1)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('belong_module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ApiManager.ModuleInfo')),
            ],
            options={
                'db_table': 'TestCaseInfo',
            },
        ),
    ]

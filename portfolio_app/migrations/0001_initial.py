# Generated by Django 3.1.4 on 2021-05-04 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.FileField(upload_to='static/images')),
                ('title', models.CharField(max_length=50)),
                ('info', models.CharField(max_length=200)),
                ('day', models.CharField(max_length=3)),
                ('month', models.CharField(max_length=10)),
                ('year', models.CharField(max_length=5)),
                ('html', models.BooleanField()),
                ('css', models.BooleanField()),
                ('javascript', models.BooleanField()),
                ('python', models.BooleanField()),
                ('database', models.BooleanField()),
                ('django', models.BooleanField()),
                ('tensorflow', models.BooleanField()),
                ('github_link', models.CharField(max_length=200)),
            ],
        ),
    ]

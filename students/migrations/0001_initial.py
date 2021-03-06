# Generated by Django 2.2.3 on 2019-07-05 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, unique=True)),
                ('total_seat', models.IntegerField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, unique=True)),
                ('relation_to_student', models.CharField(max_length=512)),
                ('mobile', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=2024)),
                ('occupation', models.CharField(blank=True, max_length=1024)),
                ('prefered_contact_time', models.CharField(blank=True, max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('roll_no', models.IntegerField(max_length=11)),
                ('class_id', models.ForeignKey(on_delete='SET_NULL', to='students.ClassName')),
                ('parent_id', models.ForeignKey(on_delete='CASCADE', to='students.Parent')),
            ],
        ),
    ]

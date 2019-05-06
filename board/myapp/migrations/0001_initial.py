# Generated by Django 2.2.1 on 2019-05-05 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titleboard', models.CharField(blank=True, max_length=50)),
                ('detail', models.TextField(max_length=100)),
                ('image', models.ImageField(upload_to='')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titleexam', models.CharField(max_length=50, null=True)),
                ('date', models.DateField()),
                ('category', models.CharField(choices=[('ENG', 'English'), ('MATH', 'Math'), ('OTHERS', 'Others')], default='ENG', max_length=10)),
                ('link', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('file', models.FileField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('role', models.CharField(max_length=1)),
            ],
        ),
    ]
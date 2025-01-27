# Generated by Django 4.2.13 on 2024-07-02 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Department Name')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, verbose_name='Username')),
                ('password', models.CharField(max_length=100, verbose_name='Password')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('gender', models.SmallIntegerField(choices=[(1, 'Male'), (2, 'Female'), (3, 'Unknown')], max_length=100, verbose_name='Gender')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.department')),
            ],
        ),
    ]

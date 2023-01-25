# Generated by Django 3.2.16 on 2023-01-24 12:07

from django.db import migrations, models
import django.db.models.deletion

#  because Error
class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_jop_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('job_type', models.CharField(choices=[('Full-Time', 'Full-Time'), ('Part-Time', 'Part-Time')], max_length=15)),
                ('description', models.TextField(max_length=1000)),
                ('published_at', models.DateTimeField(auto_now=True)),
                ('Vacancy', models.IntegerField(default=1)),
                ('salary', models.IntegerField(default=0)),
                ('experience', models.IntegerField(default=1)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.category')),
            ],
        ),
        migrations.DeleteModel(
            name='jop',
        ),
    ]

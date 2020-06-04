# Generated by Django 3.0.6 on 2020-06-04 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('questions', models.CharField(max_length=400)),
                ('priority', models.CharField(choices=[('L', 'Low'), ('M', 'Medium'), ('H', 'High')], max_length=1)),
            ],
            options={
                'verbose_name': 'The Question',
                'verbose_name_plural': "People's Question",
            },
        ),
        migrations.DeleteModel(
            name='description',
        ),
    ]

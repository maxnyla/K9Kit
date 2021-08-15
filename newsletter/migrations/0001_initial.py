# Generated by Django 3.1.7 on 2021-08-15 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newsletter_title', models.CharField(max_length=254)),
                ('newsletter_body', models.TextField(blank=True, default='', null=True)),
                ('newsletter_by', models.CharField(default='', max_length=254)),
                ('newsletter_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-newsletter_date'],
            },
        ),
    ]

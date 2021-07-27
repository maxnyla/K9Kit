# Generated by Django 3.1.7 on 2021-07-27 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_title', models.CharField(max_length=254)),
                ('review_body', models.TextField(blank=True, default='', null=True)),
                ('review_by', models.CharField(default='', max_length=254)),
                ('review_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_review', to='profiles.userprofile')),
            ],
        ),
    ]

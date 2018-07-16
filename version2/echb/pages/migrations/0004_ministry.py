# Generated by Django 2.0.6 on 2018-06-28 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20180628_1639'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ministry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('seo_keywords', models.CharField(blank=True, max_length=250, null=True)),
                ('seo_description', models.CharField(blank=True, max_length=250, null=True)),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('short_description', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('icon', models.FileField(blank=True, null=True, upload_to='ministries')),
            ],
            options={
                'verbose_name': 'служение',
                'verbose_name_plural': 'служения',
            },
        ),
    ]

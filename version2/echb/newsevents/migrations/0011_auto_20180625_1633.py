# Generated by Django 2.0.6 on 2018-06-25 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsevents', '0010_auto_20180621_1157'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='author',
        ),
        migrations.RemoveField(
            model_name='article',
            name='category',
        ),
        migrations.RemoveField(
            model_name='article',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='author',
            name='description',
        ),
        migrations.RemoveField(
            model_name='author',
            name='email',
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]

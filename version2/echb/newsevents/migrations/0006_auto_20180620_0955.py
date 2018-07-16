# Generated by Django 2.0.6 on 2018-06-20 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsevents', '0005_auto_20180619_0729'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'автор',
                'verbose_name_plural': 'авторы',
            },
        ),
        migrations.AlterModelOptions(
            name='newsitem',
            options={'ordering': ['-created'], 'verbose_name': 'новость', 'verbose_name_plural': 'новости'},
        ),
        migrations.RemoveField(
            model_name='newsitem',
            name='author',
        ),
        migrations.AlterField(
            model_name='newsitem',
            name='description',
            field=models.TextField(blank=True, help_text="Проверяйте орфографию <a href='https://advego.com/text/'>здесь</a>", null=True),
        ),
        migrations.AlterField(
            model_name='newsitem',
            name='main_image',
            field=models.FileField(blank=True, help_text='Маленькое изображение, которое будет появляться около новости', null=True, upload_to='news'),
        ),
        migrations.AlterField(
            model_name='newsitem',
            name='publication_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='newsitem',
            name='short_description',
            field=models.TextField(blank=True, help_text='Краткое описание новости', null=True),
        ),
        migrations.AlterField(
            model_name='newsitem',
            name='title',
            field=models.CharField(help_text='Введите название в нижнем регистре (кроме первой буквы)', max_length=150),
        ),
    ]

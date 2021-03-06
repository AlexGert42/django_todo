# Generated by Django 4.0.1 on 2022-01-23 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL')),
                ('priority', models.IntegerField(default=5, verbose_name='Priority')),
                ('time_create', models.TimeField(auto_now_add=True, verbose_name='Time create')),
                ('time_update', models.TimeField(auto_now=True, verbose_name='Time update')),
            ],
            options={
                'verbose_name': 'Todo',
                'verbose_name_plural': 'Todos',
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL')),
                ('content', models.TextField(max_length=1000, verbose_name='Content Text')),
                ('completed', models.BooleanField(default=False, verbose_name='Completed')),
                ('priority', models.IntegerField(default=5, verbose_name='Priority')),
                ('image', models.ImageField(blank=True, upload_to='images/%Y/%m/%d/', verbose_name='Images')),
                ('time_create', models.TimeField(auto_now_add=True, verbose_name='Time create')),
                ('time_update', models.TimeField(auto_now=True, verbose_name='Time update')),
                ('is_published', models.BooleanField(default=True, verbose_name='Published')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='item.todo', verbose_name='category')),
            ],
            options={
                'verbose_name': 'Item',
                'verbose_name_plural': 'Items',
                'ordering': ['-time_update', 'pk'],
            },
        ),
    ]

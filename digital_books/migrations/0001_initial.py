<<<<<<< HEAD
# Generated by Django 3.0.8 on 2020-07-17 17:09
=======
# Generated by Django 3.0.8 on 2020-07-17 05:42
>>>>>>> 288ec2f08e8976a47df466e82b9019db156d7d95

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('limit', models.IntegerField(default=3)),
                ('URL', models.URLField()),
                ('language', models.CharField(max_length=50)),
                ('sort_title', models.CharField(max_length=200)),
                ('author_last', models.CharField(max_length=200)),
                ('author_first', models.CharField(max_length=200)),
                ('checked_out', models.ManyToManyField(related_name='checked_out', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HoldOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digital_books.Book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('time_created',),
            },
        ),
        migrations.AddField(
            model_name='book',
            name='holds',
            field=models.ManyToManyField(blank=True, related_name='holds', through='digital_books.HoldOrder', to=settings.AUTH_USER_MODEL),
        ),
    ]

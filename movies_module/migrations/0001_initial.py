# Generated by Django 4.1.5 on 2023-07-17 16:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import embed_video.fields


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='movie_image')),
                ('name', models.CharField(max_length=100)),
                ('imdb', models.FloatField(default=0)),
                ('year', models.IntegerField()),
                ('length', models.IntegerField()),
                ('description', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
                ('local_trailer', models.FileField(default='movie_video/pexels-vision-plug-15698543_1080p.mp4', upload_to='movie_video/')),
                ('trailer', embed_video.fields.EmbedVideoField(blank=True, null=True)),
                ('country', models.ManyToManyField(to='movies_module.country')),
                ('director', models.ManyToManyField(to='movies_module.director')),
                ('genre', models.ManyToManyField(to='movies_module.genre')),
            ],
        ),
        migrations.CreateModel(
            name='MovieGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='movie_image/gallery/')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies_module.movie')),
            ],
        ),
        migrations.CreateModel(
            name='MovieComments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('num_of_like', models.IntegerField(default=0)),
                ('num_of_dislike', models.IntegerField(default=0)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies_module.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),

    ]

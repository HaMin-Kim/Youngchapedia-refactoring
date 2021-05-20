from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45, null=True)),
                ('gender', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField(null=True)),
            ],
            options={
                'db_table': 'actors',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
            ],
            options={
                'db_table': 'comments',
            },
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45, null=True)),
                ('gender', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField(null=True)),
            ],
            options={
                'db_table': 'directors',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'genres',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('korean_title', models.CharField(max_length=45)),
                ('english_title', models.CharField(max_length=45, null=True)),
                ('country', models.CharField(max_length=45)),
                ('release_date', models.DateField(null=True)),
                ('running_time', models.IntegerField()),
                ('discription', models.TextField(null=True)),
                ('audience_count', models.IntegerField()),
                ('thumbnail_img', models.URLField()),
                ('background_img', models.URLField()),
                ('netflix', models.BooleanField(default=False)),
                ('watcha', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'movies',
            },
        ),
        migrations.CreateModel(
            name='MovieGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.genre')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
            ],
            options={
                'db_table': 'movie_genres',
            },
        ),
        migrations.CreateModel(
            name='MovieDirector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.director')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
            ],
            options={
                'db_table': 'movie_directors',
            },
        ),
        migrations.CreateModel(
            name='MovieActor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.actor')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
            ],
            options={
                'db_table': 'movie_actors',
            },
        ),
        migrations.AddField(
            model_name='movie',
            name='actor',
            field=models.ManyToManyField(through='movies.MovieActor', to='movies.Actor'),
        ),
        migrations.AddField(
            model_name='movie',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='movies.category'),
        ),
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.ManyToManyField(through='movies.MovieDirector', to='movies.Director'),
        ),
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.ManyToManyField(through='movies.MovieGenre', to='movies.Genre'),
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.comment')),
            ],
            options={
                'db_table': 'likes',
            },
        ),
    ]

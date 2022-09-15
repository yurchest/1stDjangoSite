# Generated by Django 4.0.5 on 2022-07-13 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='название статьи')),
                ('content', models.TextField(verbose_name='текст статьи')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='дата публикации')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='дата изменения')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Ваше имя:')),
                ('email', models.CharField(max_length=100, verbose_name='Ваш e-mail:')),
                ('text', models.TextField(max_length=255, verbose_name='Сообщение')),
                ('published_date', models.DateTimeField(auto_now_add=True, verbose_name='дата сообщения')),
            ],
            options={
                'permissions': (('can_see_messages', 'You can see list messages'),),
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='текст новости')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='дата загрузки с сайта')),
                ('link', models.URLField(max_length=255, verbose_name='URL')),
            ],
        ),
        migrations.CreateModel(
            name='Userip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=30, verbose_name='Айпи адрес')),
                ('count', models.IntegerField(default=0, verbose_name='Визиты')),
            ],
            options={
                'verbose_name': 'Доступ к информации о пользователе',
                'verbose_name_plural': 'Доступ к информации о пользователе',
            },
        ),
        migrations.CreateModel(
            name='VisitNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0, verbose_name='Всего просмотров резюме')),
            ],
            options={
                'verbose_name': 'Всего просмотров резюме',
                'verbose_name_plural': 'Всего просмотров резюме',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=50, verbose_name='имя автора')),
                ('comment_text', models.CharField(max_length=60, verbose_name='текст комментария')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.article')),
            ],
        ),
    ]
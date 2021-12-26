from django.db import models

class Article(models.Model):
    title = models.CharField('название статьи', max_length=200)
    content = models.TextField('текст статьи')
    time_create = models.DateTimeField('дата публикации', auto_now_add=True)
    time_update = models.DateTimeField('дата изменения', auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_name = models.CharField('имя автора', max_length=50)
    comment_text = models.CharField('текст комментария',  max_length=60)
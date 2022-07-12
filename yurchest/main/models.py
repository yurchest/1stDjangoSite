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

class Contact(models.Model):
    name = models.CharField('Ваше имя:',max_length=50)
    email = models.CharField('Ваш e-mail:',max_length=100)
    text = models.TextField('Сообщение', max_length=255)
    published_date = models.DateTimeField('дата сообщения',auto_now_add=True)

    class Meta:
        permissions = (("can_see_messages", "You can see list messages"),)

    def __str__(self):
        return self.name
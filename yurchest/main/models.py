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


class VisitNumber(models.Model):
    count=models.IntegerField(verbose_name='Всего просмотров резюме',default=0)
    class Meta:
        verbose_name = 'Всего просмотров резюме'
        verbose_name_plural = verbose_name
    def __str__(self):
        return str(self.count)

class Userip(models.Model):
    ip=models.CharField(verbose_name='Айпи адрес',max_length=30)    #айпи адрес
    count=models.IntegerField(verbose_name='Визиты',default=0) # Ip посещения
    class Meta:
        verbose_name = 'Доступ к информации о пользователе'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.ip

class News(models.Model):
    content = models.TextField('текст новости')
    time_create = models.DateTimeField('дата загрузки с сайта', auto_now_add=True)
    link = models.URLField('URL',max_length = 255)

    def __str__(self):
        return self.content
from django.contrib import admin

from .models import Article, Comment, Contact, VisitNumber, Userip, News

admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Contact)
admin.site.register(VisitNumber)
admin.site.register(Userip)
admin.site.register(News)

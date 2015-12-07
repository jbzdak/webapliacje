from django.db import models


class BlogPost(models.Model):
    text = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)


class BlogComment(models.Model):
    text = models.TextField()
    owner = models.CharField(max_length=20)
    post = models.ForeignKey('BlogPost', null=False)
    posted_at = models.DateTimeField(auto_now_add=True)
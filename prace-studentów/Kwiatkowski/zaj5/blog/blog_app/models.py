from django.db import models

class BlogPost(models.Model):

  text = models.TextField()
  posted_at = models.DateTimeField(auto_now_add=True)

  class Meta:

    db_table='blog_post'
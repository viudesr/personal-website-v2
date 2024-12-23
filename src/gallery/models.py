from django.db import models

class article(models.Model):
    pub_date = models.DateTimeField("date published")
    count_views = models.IntegerField("views")

class comment(models.Model):
    pub_date = models.DateTimeField("date published")
    # author = models.
    content = models.TextField("content")
    upvotes = models.IntegerField("upvotes")
    downvotes = models.IntegerField("downvotes")

class picture(models.Model):
    pub_date = models.DateTimeField("date published")
    path = models.TextField("path")
    likes = models.IntegerField("likes")
    views = models.IntegerField("views")

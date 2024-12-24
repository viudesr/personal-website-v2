from django.db import models

class Article(models.Model):
    pub_date = models.DateTimeField("date published")
    count_views = models.IntegerField("views")
    description = models.TextField("description")

class Comment(models.Model):
    pub_date = models.DateTimeField("date published")
    # author = models.
    content = models.TextField("content")
    upvotes = models.IntegerField("upvotes")
    downvotes = models.IntegerField("downvotes")

class Picture(models.Model):
    pub_date = models.DateTimeField("date published")
    path = models.TextField("path")
    likes = models.IntegerField("likes")
    views = models.IntegerField("views")
    description = models.TextField("legend")

class Article_joint_picture(models.Model):
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)
    picture_id = models.ForeignKey(Picture, on_delete=models.CASCADE)
    picture_pos = models.IntegerField("picture position")

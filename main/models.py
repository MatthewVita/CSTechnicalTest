from django.db import models


class Topic(models.Model):
    poster = models.CharField(max_length=64)
    title = models.CharField(max_length=128)
    description = models.TextField()

class Comment(models.Model):
    poster = models.CharField(max_length=64)
    comment = models.TextField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='comments')
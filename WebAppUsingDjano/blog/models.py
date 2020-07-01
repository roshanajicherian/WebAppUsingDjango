from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # do not pass timezone.now as a function even though it is
    datePosted = models.DateTimeField(default=timezone.now)
    # CASCADE - if a user is deleted delete the post as well
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

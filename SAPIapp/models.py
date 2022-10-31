from django.db import models

# intern model
class Intern(models.Model):
    slackUsername = models.CharField(max_length=50, default="")
    backend = models.BooleanField(default="True")
    age = models.SmallIntegerField()
    bio = models.TextField()

    def __str__(self):
        return self.slackUsername
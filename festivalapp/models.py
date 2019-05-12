from django.db import models

class Fest(models.Model):

    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

class Lost(models.Model):

    title2 = models.CharField(max_length=200)
    writer2 = models.CharField(max_length=100)
    pub_date2 = models.DateTimeField('data pub')
    body2 = models.TextField()

    def __str__(self):
        return self.title2

    def summary(self):
        return self.body2[:100]

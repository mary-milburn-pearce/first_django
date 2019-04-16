from django.db import models

class Show(models.Model):
    title = models.CharField(max_length=100)
    network = models.CharField(max_length=50)
    release_date = models.DateField()
    description = models.TextField()

    def __repr__(self):
        return '%s | %s | %s | %s' % (self.title, self.network, self.release_date, self.description)

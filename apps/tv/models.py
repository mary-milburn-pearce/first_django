from django.db import models
from datetime import datetime

class TVShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 1:
            errors["title"] = "Title cannot be blank"
        if len(postData['network']) < 1:
            errors["network"] = "Network cannot be blank"
        if len(postData['rel_date']) < 1:
            errors["rel_date"] = "Release Date cannot be blank"
        else:
            d1 = datetime.strptime(postData['rel_date'], "%Y-%m-%d").date()
            if d1 > datetime.now().date():
                print("greater than today")
                errors["future_rel_date"] = "Release Date must today or in the past"
        if len(postData['desc']) > 0 and len(postData['desc']) < 10:
            errors["desc"] = "Description must be longer than 10 characters if present"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=100)
    network = models.CharField(max_length=50)
    release_date = models.DateField()
    description = models.TextField(blank=True)
    objects = TVShowManager()

    def __repr__(self):
        return f"Title: {self.title}, Network: {self.network}, Released: {self.release_date}, Description: {self.description}"

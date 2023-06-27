from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=250, db_index=True)
    email = models.EmailField()
    subject = models.CharField(max_length=120, db_index=True)
    message = models.TextField()
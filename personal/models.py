from django.db import models

class description(models.Model):
    name = models.CharField(max_length=20, name='name')
    email = models.EmailField(max_length=20, name='email')
    

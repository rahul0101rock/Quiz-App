from django.db import models


# Create your models here.

class Questions(models.Model):
    CAT_CHOICES = (
        ('python', 'Python'),
        ('django', 'Django Knowledge'),
        ('numpy', 'Numpy'),
        ('java', 'Core Java'),
    )
    question = models.CharField(max_length=250)
    option_a = models.CharField(max_length=100)
    option_b = models.CharField(max_length=100)
    option_c = models.CharField(max_length=100)
    option_d = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    catagory = models.CharField(max_length=20, choices=CAT_CHOICES)

    class Meta:
        ordering = ('-catagory',)

    def __str__(self):
        return self.question

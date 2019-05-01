from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length =100)
    firstname = models.CharField(max_length = 50)
    lastname = models.CharField(max_length = 50)
    role = models.CharField(max_length = 1)

class News(models.Model):
    news_id = models.CharField(max_length = 100)
    title = models.CharField(max_length=500)
    date = models.DateField()
    file = models.FileField(upload_to='files/',blank=False)
    detail = models.TextField(max_length = 500 , blank = True, null = True)
    def __str__(self):
        return self.title, self.date

class Board(models.Model):
    board_id = models.CharField(max_length = 100)
    detail = models.TextField(max_length = 100) 
    image = models.ImageField() 
    date = models.DateField()

class Exam (models.Model):
    exam_id = models.CharField(max_length = 100)
    detail = models.CharField(max_length=500)
    date = models.DateField()
    category = models.CharField(max_length=50)
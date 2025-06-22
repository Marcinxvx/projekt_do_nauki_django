from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    def __str__(self):
        return f'{self.name} {self.year}'

class Genre(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.name}'

class Film(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)                 #nie dodajemy null=True bo Author byl w tej samej migracji co Film
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, null=True)#dodajemy null=True dlatego dopisalismy te kolumne pozniej do Film, wiec musimy czyms te kolumne wypełnić
    genres = models.ManyToManyField(Genre)
    def __str__(self):
        return f'{self.title}'

class Distributor(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()

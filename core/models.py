from django.db import models

# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name="movies")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="movies/", blank=True)

    def __str__(self):
        return self.name


class Feedback(models.Model):
    title = models.CharField(max_length=200)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="feedbacks")

    def __str__(self):
        return self.title

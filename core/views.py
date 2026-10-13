from django.shortcuts import get_object_or_404, redirect, render

from .models import Feedback, Genre, Movie


def index(request):
    return render(request, "index.html")


def add_movie(request):
    if request.method == "POST":
        Movie.objects.create(
            name=request.POST.get("name"),
            description=request.POST.get("description"),
            genre_id=request.POST.get("genre_id"),
            image=request.FILES.get("image"),
        )
        return redirect("get_all_movies")

    genres = Genre.objects.all()
    return render(request, "add_movie.html", {"genres": genres})


def get_all_movies(request):
    movies = Movie.objects.select_related("genre").all()
    return render(request, "movies.html", {"movies": movies})


def coming_soon(request):
    return render(request, "coming_soon.html")


def cinema(request):
    return render(request, "cinema.html")


def update_movie(request, id):
    movie = get_object_or_404(Movie, id=id)

    if request.method == "POST":
        movie.name = request.POST.get("name")
        movie.description = request.POST.get("description")
        movie.genre_id = request.POST.get("genre_id")
        if request.FILES.get("image"):
            movie.image = request.FILES["image"]
        movie.save()
        return redirect("get_all_movies")

    genres = Genre.objects.all()
    return render(request, "update_movie.html", {"movie": movie, "genres": genres})


def delete_movie(request, id):
    movie = get_object_or_404(Movie, id=id)

    if request.method == "POST":
        movie.delete()
        return redirect("get_all_movies")

    return render(request, "delete_movie.html", {"movie": movie})



def add_feedback(request):
    if request.method == "POST":
        Feedback.objects.create(
            title=request.POST.get("title"),
            movie_id=request.POST.get("movie_id"),
        )
        return redirect("get_all_movies")

    movies = Movie.objects.all()
    return render(request, "add_feedback.html", {"movies": movies})


def update_feedback(request, id):
    feedback = get_object_or_404(Feedback, id=id)

    if request.method == "POST":
        feedback.title = request.POST.get("title")
        feedback.movie_id = request.POST.get("movie_id")
        feedback.save()
        return redirect("get_all_movies")

    movies = Movie.objects.all()
    return render(
        request,
        "update_feedback.html",
        {"feedback": feedback, "movies": movies},
    )


def delete_feedback(request, id):
    feedback = get_object_or_404(Feedback, id=id)

    if request.method == "POST":
        feedback.delete()
        return redirect("get_all_movies")

    return render(request, "delete_feedback.html", {"feedback": feedback})



def add_genre(request):
    if request.method == "POST":
        Genre.objects.create(name=request.POST.get("name"))
        return redirect("get_all_movies")

    return render(request, "add_genre.html")


def update_genre(request, id):
    genre = get_object_or_404(Genre, id=id)

    if request.method == "POST":
        genre.name = request.POST.get("name")
        genre.save()
        return redirect("get_all_movies")

    return render(request, "update_genre.html", {"genre": genre})


def delete_genre(request, id):
    genre = get_object_or_404(Genre, id=id)

    if request.method == "POST":
        genre.delete()
        return redirect("get_all_movies")

    return render(request, "delete_genre.html", {"genre": genre})

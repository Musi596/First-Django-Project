from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add_movie/", views.add_movie, name="add_movie"),
    path("get_all_movies/", views.get_all_movies, name="get_all_movies"),
    path("coming-soon/", views.coming_soon, name="coming_soon"),
    path("cinema/", views.cinema, name="cinema"),
    path("update_movie/<int:id>/", views.update_movie, name="update_movie"),
    path("delete_movie/<int:id>/", views.delete_movie, name="delete_movie"),
    path("add_feedback/", views.add_feedback, name="add_feedback"),
    path("update_feedback/<int:id>/", views.update_feedback, name="update_feedback"),
    path("delete_feedback/<int:id>/", views.delete_feedback, name="delete_feedback"),
    path("add_genre/", views.add_genre, name="add_genre"),
    path("update_genre/<int:id>/", views.update_genre, name="update_genre"),
    path("delete_genre/<int:id>/", views.delete_genre, name="delete_genre"),
]

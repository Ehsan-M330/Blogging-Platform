from django.urls import path
from . import views

urlpatterns = [
    path("posts/", view=views.create_post),
    path("posts/<int:id>/", view=views.update_post),
]

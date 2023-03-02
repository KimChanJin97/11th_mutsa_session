from django.urls import path
from .views import home, detail, new, create, edit, update, delete

app_name = "blog"

urlpatterns = [
    # READ : list view
    path("", home, name="home"),
    # READ : detail view
    path("blog/<int:id>", detail, name="detail"),
    # CREATE
    path("new", new, name="new"),
    path("blog/create", create, name="create"),
    # UPDATE
    path("blog/edit/<int:id>", edit, name="edit"),
    path("blog/update/<int:id>", update, name="update"),
    # DELETE
    path("blog/delete/<int:id>", delete, name="delete"),
]
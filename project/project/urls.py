from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    # blog 앱
    path("", include("blog.urls")),
    # user 앱
    path("user/", include("user.urls")),
]



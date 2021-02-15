from django.urls import path
from .views import project_index, project_detail, home

urlpatterns = [
    path('', home, name='Home'),
    path("projects/", project_index, name="project_index"),
    path("projects/<int:pk>/", project_detail, name="project_detail"),
]

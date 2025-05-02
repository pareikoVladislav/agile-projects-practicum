from django.urls import path

from projects.views.tags import (
    TagsListCreateAPIView,
    TagsRetrieveUpdateDeleteAPIView
)
from projects.views.projects import (
    ProjectsListCreateAPIView,
    ProjectRetrieveUpdateDeleteAPIView,
    ProjectFilesListGenericView
)
from projects.views.task import AllTasksListGenericView


urlpatterns = [
    path('tags/', TagsListCreateAPIView.as_view()),
    path('tags/<int:pk>/', TagsRetrieveUpdateDeleteAPIView.as_view()),

    path('projects/', ProjectsListCreateAPIView.as_view()),
    path('projects/<int:pk>/', ProjectRetrieveUpdateDeleteAPIView.as_view()),

    path('projects-files/', ProjectFilesListGenericView.as_view()),
    path('tasks/', AllTasksListGenericView.as_view()),

]

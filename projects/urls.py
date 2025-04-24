from django.urls import path
from projects.views.tags import TagsCreateListAPIView, TagsRetrieveUpdateDeleteAPIView
from projects.views.projects import ProjectsListAPIView
urlpatterns = [
    path('tags/', TagsCreateListAPIView.as_view()),
    path('tags/<int:pk>/', TagsRetrieveUpdateDeleteAPIView.as_view()),

    path('projects/', ProjectsListAPIView.as_view()),
]


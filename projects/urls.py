from django.urls import path
from projects.views.tags import TagsCreateListAPIView

urlpatterns = [
    path('tags/', TagsCreateListAPIView.as_view()),

]

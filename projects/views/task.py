from rest_framework.generics import ListCreateAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import SAFE_METHODS

from projects.serializers.tasks import AllTasksSerializer, CreateTaskSerializer
from projects.models.task import Task



class AllTasksListGenericView(ListCreateAPIView):
    pagination_class = LimitOffsetPagination
    def get_queryset(self):
        q = Task.objects.all()
        project_name = self.request.query_params.get('project_name')
        assignee_email = self.request.query_params.get('assignee_email')
        if project_name:
            q = q.filter(project__name__iexact=project_name)
        if assignee_email:
            q = q.filter(assignee__email__iexact=assignee_email)
        return q
        
    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return AllTasksSerializer
        return CreateTaskSerializer
            
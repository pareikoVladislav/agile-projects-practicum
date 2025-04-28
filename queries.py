import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_config.settings')
django.setup()


from projects.models import Project, ProjectFile, Task, Tag, User
# ==================================================================================

# TASK 1
# ==================================================================================
# tags_list = [
#     Tag(name='Backend'),
#     Tag(name='Frontend'),
#     Tag(name='QA'),
#     Tag(name='Design'),
#     Tag(name='DevOPS')
# ]
#
# Tag.objects.bulk_create(tags_list)




# ==================================================================================

# TASK 2
# ==================================================================================

# [
#     'TIGER', 'THIS IS A FIRST PROJECT',
#     'SapHYR INC', 'THE BEST PROJECT EVER'
# ]

# projects = [
#     Project(name="TIGER", description="THIS IS A FIRST PROJECT"),
#     Project(name="SapHYR INC", description="THE BEST PROJECT EVER")
# ]
#
# Project.objects.bulk_create(projects)
#



# ==================================================================================

# TASK 3
# ==================================================================================

# tiger_project = Project.objects.get(name="TIGER")
# saphyr_project = Project.objects.get(name="SapHYR INC")
#
# # --- Файлы для проекта Tiger ---
# ProjectFile.objects.bulk_create([
#     ProjectFile(name='THE FIRST FILE', file='projects/tiger/THE_first_file.doc'),
#     ProjectFile(name='IMPORTANT DOCUMENT', file='projects/tiger/important_doc_9s9fh7g4hd4hgf6.pdf'),
#     ProjectFile(name='README', file='projects/tiger/README.md'),
# ])
#
# tiger_files = list(ProjectFile.objects.filter(file__startswith='projects/tiger/'))
#
# tiger_project.files.add(*tiger_files)  # заменит текущие связи на эти
#
# # --- Файлы для проекта Saphyr ---
# ProjectFile.objects.bulk_create([
#     ProjectFile(name='README', file='projects/saphyr/README.md'),
#     ProjectFile(name='DB_DIAGRAMM', file='projects/saphyr/db_schema_h3g45f67d.drawio'),
#     ProjectFile(name='budget', file='projects/saphyr/proj_budget.xlsx'),
# ])
#
# saphyr_files = list(ProjectFile.objects.filter(file__startswith='projects/saphyr/'))
#
# saphyr_project.files.add(*saphyr_files)



# ==================================================================================

# TASK 4
# ==================================================================================
# backend_dev = User(username='backend_dev', email='backend.dev@gmail.com', position="PROGRAMMER")
# backend_dev.set_password("sd7f6g5fsfd")
# backend_dev.save()
#
#
# frontend_dev = User(username='frontend_dev', email='frontend.dev@gmail.com', position="PROGRAMMER")
# frontend_dev.set_password("sd7f6g5fsfd")
# frontend_dev.save()
#
# designer_dev = User(username='designer', email='omg.designer@icloud.com', position="PROGRAMMER")
# designer_dev.set_password("sd7f6g5fsfd")
# designer_dev.save()
#
# devops_dev = User(username='devops', email='devops.3000@icloud.com', position="PROGRAMMER")
# devops_dev.set_password("sd7f6g5fsfd")
# devops_dev.save()
#
# qa_dev = User(username='qa_dev', email='qa.doesntmetter@gmail.com', position="QA")
# qa_dev.set_password("sd7f6g5fsfd")
# qa_dev.save()

# ==================================================================================

# TASK 5
# ==================================================================================

# from django.utils import timezone
# import datetime
#
# tiger_project = Project.objects.get(name="TIGER")
# saphyr_project = Project.objects.get(name="SapHYR INC")
#
# backend_dev = User.objects.get(username="backend_dev")
# devops_dev = User.objects.get(username="devops")
# designer_dev = User.objects.get(username="designer")
# frontend_dev = User.objects.get(username="frontend_dev")
# qa_dev = User.objects.get(username="qa_dev")
#
#
# tiger_tasks = Task.objects.bulk_create([
#     Task(title="Create new endpoint to get all project's tasks", priority=5, project=tiger_project, assignee=backend_dev, due_date=timezone.now() + datetime.timedelta(days=1)),
#     Task(title="Update schema", priority=5, project=tiger_project, assignee=backend_dev, due_date=timezone.now() + datetime.timedelta(days=3)),
#     Task(title="Connect new microservice", priority=3, project=tiger_project, assignee=devops_dev, due_date=timezone.now() + datetime.timedelta(days=20)),
#     Task(title="Update Stage build", priority=3, project=tiger_project, assignee=devops_dev, due_date=timezone.now() + datetime.timedelta(days=15)),
#     Task(title="Update UX to mobile app", priority=4, project=tiger_project, assignee=designer_dev, due_date=timezone.now() + datetime.timedelta(days=10)),
#     Task(title="Update 404 page", priority=5, project=tiger_project, assignee=frontend_dev, due_date=timezone.now() + datetime.timedelta(days=2)),
#     Task(title="Test new functionality", priority=4, project=tiger_project, assignee=qa_dev, due_date=timezone.now() + datetime.timedelta(days=7)),
#     Task(title="test register form", priority=3, project=tiger_project, assignee=qa_dev, due_date=timezone.now() + datetime.timedelta(days=14)),
# ])
#
# saphyr_tasks = Task.objects.bulk_create([
#     Task(title="Update new endpoint to delete panel", priority=5, project=saphyr_project, assignee=backend_dev, due_date=timezone.now() + datetime.timedelta(days=1)),
#     Task(title="Update DB schema", priority=5, project=saphyr_project, assignee=backend_dev, due_date=timezone.now() + datetime.timedelta(days=2)),
#     Task(title="Connect new Azure storage", priority=3, project=saphyr_project, assignee=devops_dev, due_date=timezone.now() + datetime.timedelta(days=11)),
#     Task(title="Update Build pipelines", priority=4, project=saphyr_project, assignee=devops_dev, due_date=timezone.now() + datetime.timedelta(days=6)),
#     Task(title="Update UI to desktop app", priority=4, project=saphyr_project, assignee=designer_dev, due_date=timezone.now() + datetime.timedelta(days=5)),
#     Task(title="Update redirect page", priority=5, project=saphyr_project, assignee=frontend_dev, due_date=timezone.now() + datetime.timedelta(days=3)),
#     Task(title="Test new mobile functionality", priority=4, project=saphyr_project, assignee=qa_dev, due_date=timezone.now() + datetime.timedelta(days=4)),
#     Task(title="test update account form", priority=3, project=saphyr_project, assignee=qa_dev, due_date=timezone.now() + datetime.timedelta(days=9)),
# ])



# ==================================================================================

# TASK 6
# ==================================================================================
# tiger_task_1 = Task.objects.get(id=1)
# tiger_task_2 = Task.objects.get(id=2)
# tiger_task_3 = Task.objects.get(id=3)
# tiger_task_4 = Task.objects.get(id=4)
# tiger_task_5 = Task.objects.get(id=5)
# tiger_task_6 = Task.objects.get(id=6)
# tiger_task_7 = Task.objects.get(id=7)
# tiger_task_8 = Task.objects.get(id=8)
#
# saphyr_task_1 = Task.objects.get(id=9)
# saphyr_task_2 = Task.objects.get(id=10)
# saphyr_task_3 = Task.objects.get(id=11)
# saphyr_task_4 = Task.objects.get(id=12)
# saphyr_task_5 = Task.objects.get(id=13)
# saphyr_task_6 = Task.objects.get(id=14)
# saphyr_task_7 = Task.objects.get(id=15)
# saphyr_task_8 = Task.objects.get(id=16)
#
#
# back_tag = Tag.objects.get(name="Backend")
# front_tag = Tag.objects.get(name="Frontend")
# devops_tag = Tag.objects.get(name="DevOPS")
# design_tag = Tag.objects.get(name="Design")
# qa_tag = Tag.objects.get(name="Q&A")
#
#
# tiger_task_1.tags.add(back_tag)
# tiger_task_2.tags.add(back_tag)
# tiger_task_3.tags.add(devops_tag)
# tiger_task_4.tags.add(devops_tag)
# tiger_task_5.tags.add(design_tag)
# tiger_task_5.tags.add(design_tag)
# tiger_task_6.tags.add(front_tag)
# tiger_task_7.tags.add(qa_tag)
# tiger_task_8.tags.add(qa_tag)
#
#
# saphyr_task_1.tags.add(back_tag)
# saphyr_task_2.tags.add(back_tag)
# saphyr_task_3.tags.add(front_tag)
# saphyr_task_4.tags.add(front_tag)
# saphyr_task_5.tags.add(design_tag)
# saphyr_task_6.tags.add(design_tag)
# saphyr_task_7.tags.add(qa_tag)
# saphyr_task_8.tags.add(qa_tag)



# ==================================================================================

# TASK 7

# Получение тегов
#
# Импортируйте модели тегов Tag.
# Напишите запрос, который позволит получить список всех тегов.
# Выведите имя каждого тега.
# Получите самый первый тег.
# Получите самый последний тег.
# Получите кол-во всех тегов.

# ==================================================================================
# all_tags = Tag.objects.all()
# for tag in all_tags:
#     print(tag.name)
#
# last_tag = Tag.objects.last()
# print(last_tag.name)
#
#
# first_tag = Tag.objects.first()
# print(first_tag.name)
#
#
# count_of_tags = Tag.objects.count()
# print(count_of_tags)



# ==================================================================================

# TASK 8

# Проверка существования тега с определенным именем
#
# Напишите запрос, который будет искать тэг по определённому имени
# Проверьте наличие такого тега методом, который выдаёт True или False на наличие объекта.


# ==================================================================================
# tag_exists = Tag.objects.filter(name='SUPERTAG').exists()
#
# print(tag_exists)


# ==================================================================================

# TASK 9

# Фильтрация тегов по имени
#
# Напишите запрос, который позволит получить теги, у которых в имени будет совпадение по переданной строке, например: “...Tag”
# Выведите имена всех этих тегов.


# ==================================================================================
# tags_by_str_match = Tag.objects.filter(name__icontains='e')
# print(tags_by_str_match)
#
#
# for tag in tags_by_str_match:
#     print(tag.name)


# ==================================================================================

# TASK 10

# Фильтрация проектов по дате создания
#
# Импортируйте модуль datetime и модель Project.
# Создайте объект даты, по которой нужно сделать поиск.
# Напишите запрос, который позволит получить список проектов, которые равны или старше переданной даты создания.
# Выведите имена таких проектов.


# ==================================================================================
# import datetime
#
# required_date = datetime.datetime(2023, 1, 1).astimezone()
#
# required_projects = Project.objects.filter(date_started__gt=required_date)
#
# print(required_projects)



# ==================================================================================

# TASK 11

# Использование Q-класса для комбинированных условий
#
# Импортируйте модель Project.
# Напишите запрос, который позволит получить необходимые проекты:
# Реализуйте фильтрацию, которая будет проходить два условия:
# Проекты, равные или больше указанной даты
# Проекты, у которых в имени есть строка ‘TI’
# Выведите имена таких проектов.


# ==================================================================================
# from django.db.models import Q
#
# required_date = datetime.datetime(2023, 1, 1).astimezone()
#
# specifying_projects = Project.objects.filter(Q(date_started__gt=required_date) & Q(name__icontains='TI'))
#
# print(specifying_projects)
#
# print(specifying_projects[0].name)
# print(specifying_projects[0].description)

# ==================================================================================

# TASK 12

# Получение списка всех файлов для конкретного проекта
#
# Напишите запрос, который позволит получить список всех файлов, которые привязаны к конкретному проекту. Поиск произведите по имени проекта.
# Выведите только пути к каждому файлу.


# ==================================================================================
# required_files = ProjectFile.objects.filter(projects__name__contains='TIGER')
#
# print(required_files)



# ==================================================================================

# TASK 13

# Фильтрация задач по статусу и приоритету
#
# Напишите запрос, который поможет получить только те задачи, у которых:
# Статус “new”
# Приоритетность “Critical”
# Выведите информацию по каждой такой задаче:
# Название
# Статус
# Приоритетность
# Дата, когда задача должна быть сдана
# Email сотрудника, за которым закреплена эта задача


# ==================================================================================
# from projects.choices import Priorities
# from django.db import connection, reset_queries
# import time
#
# reset_queries()
# start = time.time()
#
# req_priority = Priorities.from_label("High").db_value
#
# required_tasks = Task.objects.filter(status='NEW', priority=req_priority)
#
#
# for obj in required_tasks:
#    print("=" * 50)
#    print(obj.title)
#    print(obj.status)
#    print(obj.priority)
#    print(obj.due_date)
#    print(obj.assignee.email)
#    print("=" * 50)
#
# end = time.time()
#
# for query in connection.queries:
#     print(query["sql"])
#
# print(f"Total Queries: {len(connection.queries)}")
# print(f"Execution time: {end - start}")

# ==================================================================================















# ==================================================================================
# ==================================================================================


# ==================================================================================
# ==================================================================================

# Получение списка всех тегов и создание нового тега


# serializers.py

from rest_framework import serializers
# from rest_framework.validators import UniqueValidator

from projects.models import Tag


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class TagCreateUpdateSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(
    #     required=True,
    #     min_length=2,
    #     validators=[
    #         UniqueValidator(
    #             queryset=Tag.objects.all(),
    #             message="Tag with this name already created."
    #         )
    #     ]
    # )

    class Meta:
        model = Tag
        fields = '__all__'

    def validate_name(self, value: str=None) -> str:
        if not value:
            raise serializers.ValidationError(
                'This field is required.'
            )

        if not isinstance(value, str):
            raise serializers.ValidationError(
                'This field must be a valid string.'
            )

        if len(value) < 2:
            raise serializers.ValidationError(
                'The length of this field must be at least 2 characters.'
            )

        return value

    def create(self, validated_data: dict[str, str | int]) -> Tag:
        tag_name_exists = Tag.objects.filter(
            name=validated_data['name']
        ).exists()

        if tag_name_exists:
            raise serializers.ValidationError(
                "Tag with this name already created."
            )

        return Tag.objects.create(**validated_data)

    def update(self, instance: Tag, validated_data: dict[str, str | int]) -> Tag:
        tag_name_exists = Tag.objects.exclude(id=instance.pk).filter(
            name=validated_data['name']
        ).exists()

        if tag_name_exists:
            raise serializers.ValidationError(
                "Tag with this name already created."
            )

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()

        return instance



# ---------------------------------------------------

# views.py

from django.db.models import QuerySet
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

from projects.models import Tag
from projects.serializers.tags import (
    TagsSerializer,
    TagCreateUpdateSerializer
)


class TagsListCreateAPIView(APIView):
    def get_objects(self) -> QuerySet:
        return Tag.objects.all()

    def get(self, request: Request, *args, **kwargs) -> Response:
        tags = self.get_objects()

        if not tags.exists():
            return Response(
                data=[],
                status=status.HTTP_204_NO_CONTENT
            )

        serializer = TagsSerializer(tags, many=True)

        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )

    def post(self, request: Request, *args, **kwargs) -> Response:
        """
        {
            "name": "HR"
        }
        """
        serializer = TagCreateUpdateSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        return Response(
            data=serializer.data,
            status=status.HTTP_201_CREATED
        )




# ---------------------------------------------------


# urls.py

from django.urls import path

from projects.views.tags import TagsListCreateAPIView

urlpatterns = [
    path('tags/', TagsListCreateAPIView.as_view())
]



# ==================================================================================
# ==================================================================================


# Получение, обновление и удаление тега

# serializers.py (THE SAME)

# ---------------------------------------------------

# views.py

class TagsRetrieveUpdateDeleteAPIView(APIView):
    def get_object(self, pk: int) -> Tag:
        return get_object_or_404(Tag, pk=pk)

    def get(self, request: Request, *args, **kwargs) -> Response:
        tag = self.get_object(pk=kwargs['pk'])

        serializer = TagsSerializer(tag)

        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )

    def put(self, request: Request, *args, **kwargs) -> Response:
        tag = self.get_object(pk=kwargs['pk'])

        serializer = TagCreateUpdateSerializer(instance=tag, data=request.data)

        if not serializer.is_valid():
            return Response(
                data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer.save()

        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )

    def delete(self, request: Request, *args, **kwargs) -> Response:
        tag = self.get_object(pk=kwargs['pk'])

        tag.delete()

        return Response(
            data={"message": "Tag was deleted successfully."},
            status=status.HTTP_204_NO_CONTENT
        )


# ---------------------------------------------------


# urls.py

from django.urls import path

from projects.views.tags import (
    TagsListCreateAPIView,
    TagsRetrieveUpdateDeleteAPIView
)


urlpatterns = [
    path('tags/', TagsListCreateAPIView.as_view()),
    path('tags/<int:pk>/', TagsRetrieveUpdateDeleteAPIView.as_view())
]





# ==================================================================================
# ==================================================================================


# Задача 7: Получение списка проектов и создание нового проекта


# serializers.py

from rest_framework import serializers

from projects.models import Project


class ProjectsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name', 'date_started')

class CreateProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('name', 'description', 'date_started')
        read_only_fields = ('date_started', )

    def validate_description(self, value: str) -> str:
        if len(value) < 30:
            raise serializers.ValidationError(
                "Description must be at least 30 characters long"
            )

        return value


# ---------------------------------------------------



# views.py

from datetime import datetime, timedelta

from django.db.models import QuerySet
from django.utils import timezone

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.exceptions import ValidationError

from projects.models import Project
from projects.serializers.projects import (
    ProjectsListSerializer,
    CreateProjectSerializer
)


class ProjectsListCreateAPIView(APIView):
    DATE_FORMAT = '%Y-%m-%d'

    def parse_date(self, date_str: str, name: str) -> timezone.datetime:
        try:
            # Парсим строку в naïve datetime
            naive = datetime.strptime(date_str, self.DATE_FORMAT)
        except ValueError:
            raise ValidationError({name: f'Неверный формат даты, ожидается YYYY-MM-DD.'})
        # Делаем aware по текущему сдвигу
        return timezone.make_aware(naive)

    def get_objects(self, date_from: str = None, date_to: str = None):
        qs = Project.objects.all()

        # Фильтрация по дате "от"
        if date_from:
            dt_from = self.parse_date(date_from, 'date_from')
            qs = qs.filter(date_started__gte=dt_from)

        # Фильтрация по дате "до"
        if date_to:
            dt_to = self.parse_date(date_to, 'date_to')
            # Чтобы включить весь день date_to, добавим 23:59:59.999999
            dt_to = dt_to + timedelta(days=1) - timedelta(microseconds=1)
        else:
            # Если пользователь не передал date_to, ставим сейчас
            dt_to = timezone.now()

        qs = qs.filter(date_started__lte=dt_to)
        return qs

    def get(self, request: Request) -> Response:
        date_from = request.query_params.get('date_from')
        date_to = request.query_params.get('date_to')

        projects = self.get_objects(date_from, date_to)

        if not projects.exists():
            return Response(
                data=[],
                status=status.HTTP_204_NO_CONTENT
            )

        serializer = ProjectsListSerializer(projects, many=True)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )

    def post(self, request: Request) -> Response:
        serializer = CreateProjectSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response(
                serializer.validated_data,
                status=status.HTTP_201_CREATED,
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


# ---------------------------------------------------



# urls.py

from django.urls import path

from projects.views.tags import (
    TagsListCreateAPIView,
    TagsRetrieveUpdateDeleteAPIView
)
from projects.views.projects import (
    ProjectsListCreateAPIView
)


urlpatterns = [
    path('tags/', TagsListCreateAPIView.as_view()),
    path('tags/<int:pk>/', TagsRetrieveUpdateDeleteAPIView.as_view()),
    path('projects/', ProjectsListCreateAPIView.as_view())
]








# ==================================================================================
# ==================================================================================


# Задача 8: Получение, обновление и удаление проекта


# serializers.py


class ProjectDetailSerializer(serializers.ModelSerializer):
   class Meta:
       model = Project
       fields = ('id', 'name', 'description', 'count_of_files')




# ---------------------------------------------------



# views.py

class ProjectRetrieveUpdateDeleteAPIView(APIView):
   def get_object(self, pk: int) -> Project:
       return get_object_or_404(Project, pk=pk)

   def get(self, request: Request, pk: int) -> Response:
       project = self.get_object(pk=pk)
       serializer = ProjectDetailSerializer(project)

       return Response(
           serializer.data,
           status=status.HTTP_200_OK,
       )

   def put(self, request: Request, pk: int) -> Response:
       project = self.get_object(pk=pk)

       serializer = CreateProjectSerializer(
           instance=project,
           data=request.data,
           partial=True
       )

       if serializer.is_valid(raise_exception=True):
           serializer.save()
           return Response(
               serializer.validated_data,
               status=status.HTTP_200_OK,
           )

       return Response(
           serializer.errors,
           status=status.HTTP_400_BAD_REQUEST,
       )

   def delete(self, request: Request, pk: int) -> Response:
       project = self.get_object(pk=pk)
       project.delete()

       return Response(
           data={
               "message": "Project was deleted successfully"
           },
           status=status.HTTP_200_OK,
       )



# ---------------------------------------------------



# urls.py

from django.urls import path

from projects.views.tags import (
    TagsListCreateAPIView,
    TagsRetrieveUpdateDeleteAPIView
)
from projects.views.projects import (
    ProjectsListCreateAPIView,
    ProjectRetrieveUpdateDeleteAPIView
)


urlpatterns = [
    path('tags/', TagsListCreateAPIView.as_view()),
    path('tags/<int:pk>/', TagsRetrieveUpdateDeleteAPIView.as_view()),
    path('projects/', ProjectsListCreateAPIView.as_view()),
    path('projects/<int:pk>/', ProjectRetrieveUpdateDeleteAPIView.as_view())
]



# ==================================================================================
# ==================================================================================


# Задача 9: Работа с файлами


# utils/upload_file_helper.py

import os
from pathlib import Path

from django.utils.text import slugify

ALLOWED_EXTENSIONS = ['.csv', '.doc', '.pdf', '.xlsx', '.py']


def check_extension(filename):
   return Path(filename).suffix.lower() in ALLOWED_EXTENSIONS


def check_file_size(file, required_size=2):
   file_size = file.size / (1024 * 1024)

   if file_size > required_size:
       return False

   return True


def create_file_path(project_name: str, original_filename: str) -> str:
    ext = Path(original_filename).suffix.lower()
    name = Path(original_filename).stem
    safe_proj = slugify(project_name)
    safe_name = slugify(name)
    return str(Path('documents') / safe_proj / f'{safe_name}{ext}')


def save_file(file_path, file_content):
   os.makedirs(os.path.dirname('documents/'), exist_ok=True)
   with open(file_path, 'wb') as f:
       for chunk in file_content.chunks():
           f.write(chunk)

   return file_path




# ---------------------------------------------------


# serializers.py

class CreateProjectFileSerializer(serializers.ModelSerializer):
    project_id = serializers.PrimaryKeyRelatedField(
        queryset=Project.objects.all(),
        write_only=True,
    )

    class Meta:
        model = ProjectFile
        fields = ('project_id',)

    def validate(self, attrs):
        raw = self.context.get('raw_file')
        if raw is None:
            raise serializers.ValidationError({"file": "File is required."})

        if not raw.name.isascii():
            raise serializers.ValidationError({"file": "Filename must be ASCII."})

        if not check_extension(raw.name):
            raise serializers.ValidationError(
                {"file": f"Valid file extensions: {ALLOWED_EXTENSIONS}"}
            )

        if not check_file_size(raw):
            raise serializers.ValidationError(
                {"file": "File size is too large (2 MB max)."}
            )

        return attrs

    def create(self, validated_data):
        project = validated_data.pop('project_id')
        raw_file = self.context['raw_file']
        name = raw_file.name

        file_path = create_file_path(
            project_name=project.name,
            original_filename=name
        )

        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        save_file(
            file_path=file_path,
            file_content=raw_file
        )

        project_file = ProjectFile.objects.create(
            name=name,
            file=file_path
        )

        project_file.projects.add(project)

        return project_file



# ---------------------------------------------------



# views.py

class ProjectFileListCreateAPIView(APIView):
   def get_objects(self, project_name=None):
       if project_name:
           project_file = ProjectFile.objects.filter(
               projects__name=project_name
           )
           return project_file

       return ProjectFile.objects.all()

   def get(self, request: Request) -> Response:
       project_name = request.query_params.get('project')

       project_files = self.get_objects(project_name)

       if not project_files.exists():
           return Response(
               data=[],
               status=status.HTTP_204_NO_CONTENT
           )

       serializer = AllProjectFilesSerializer(project_files, many=True)

       return Response(
           serializer.data,
           status=status.HTTP_200_OK
       )

   def post(self, request: Request) -> Response:
       file_content = request.FILES.get("file")

       serializer = CreateProjectFileSerializer(
           data=request.data,
           context={
               "raw_file": file_content,
           }
       )

       if serializer.is_valid(raise_exception=True):
           serializer.save()

           return Response(
               data={
                   "message": "File upload successfully"
               },
               status=status.HTTP_200_OK
           )

       else:
           return Response(
               data=serializer.errors,
               status=status.HTTP_400_BAD_REQUEST
           )



# ---------------------------------------------------



# urls.py


from django.urls import path

from projects.views.tags import (
    TagsListCreateAPIView,
    TagsRetrieveUpdateDeleteAPIView
)
from projects.views.projects import (
    ProjectsListCreateAPIView,
    ProjectRetrieveUpdateDeleteAPIView
)
from projects.views.project_files import (
    ProjectFileListCreateAPIView
)


urlpatterns = [
    path('tags/', TagsListCreateAPIView.as_view()),
    path('tags/<int:pk>/', TagsRetrieveUpdateDeleteAPIView.as_view()),
    path('projects/', ProjectsListCreateAPIView.as_view()),
    path('projects/<int:pk>/', ProjectRetrieveUpdateDeleteAPIView.as_view()),
    path('files/', ProjectFileListCreateAPIView.as_view()),
]


# ==================================================================================
# ==================================================================================


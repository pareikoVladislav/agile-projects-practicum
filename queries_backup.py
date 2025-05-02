#Зайдите в Django shell консоль.
#Импортируйте модель Tag.
#Создайте объекты тэгов по направлениям:
#Backend
#Frontend
#Q&A
#Design
#DevOPS
#Сохраните изменения в базу данных.

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_config.settings')
django.setup()


#from projects.models import Tag

# Вариант 1
#Tag.objects.create(
 #   name="Backend"
#)

# Вариант 2
#tag = Tag(
 #   name="Frontend"
#)

#tag.save()


# Вариант 3
#tags = [
   # Tag(name="Q&A"),
  #  Tag(name="Design"),
 #   Tag(name="DevOPS"),
#]

#Tag.objects.bulk_create(tags)

from projects.models.project import Project

#created_projects = [
#    Project(name="TIGER", description="THIS IS A FIRST PROJECT"),
#    Project(name="SapHYR INC", description="THE BEST PROJECT EVER") ,
#]

#Project.objects.bulk_create(created_projects)

#Импортируйте модели Project, ProjectFile
#Создайте несколько записей файлов для каждого из существующих проектов.
#Для каждого объекта проекта, созданного ранее, добавьте объекты созданных файлов методом add().
#Убедитесь, что данные были созданы и сохранены в базу данных.


from projects.models import *

#projects = Project.objects.all()
#files: list[ProjectFile] = [
#    ProjectFile(name='file1', file='projects/tiger/file1.txt'),
#    ProjectFile(name='file2', file='projects/tiger/file2.txt'),
#    ProjectFile(name='file3', file="projects/tiger/file3.txt"),
#    ProjectFile(name='file4', file="projects/tiger/file4.txt"),
#]
#
#
#ProjectFile.objects.bulk_create(files)
#
#
#project = projects[0]
#project.files.add(*files)
#
#
#files_saphire: list[ProjectFile] = [
#    ProjectFile(name='file1', file='projects/saphire/file1.txt'),
#    ProjectFile(name='file2', file='projects/saphire/file2.txt'),
#    ProjectFile(name='file3', file="projects/saphire/file3.txt"),
#    ProjectFile(name='file4', file="projects/saphire/file4.txt"),
#]
#ProjectFile.objects.bulk_create(files_saphire)


#proj_saphire = projects[1]
#proj_saphire.files.add(*files_saphire)

# Получение тегов
#
# Импортируйте модели тегов Tag.
from projects.models import Tag
## Напишите запрос, который позволит получить список всех тегов.
#
#tag_list = Tag.objects.all()
#for tag in tag_list:
#    print(tag.name)
#

# Выведите имя каждого тега.
# Получите самый последний тег.
# Получите кол-во всех тегов.
# Получите самый первый тег.
#first_tag = Tag.objects.first()
#last_tag = Tag.objects.last()
#count_tags =tag_list.count()
#print(count_tags)
#print(first_tag.name)
#print(last_tag.name)


# Фильтрация тегов по имени
#
# Напишите запрос, который позволит получить теги, у которых в имени будет совпадение по переданной строке, например: “...Tag”
# Выведите имена всех этих тегов.

#from projects.models.tag import Tag
#
#req_tags = Tag.objects.filter(name__icontains="op")
#for tag in req_tags:
#    print(tag.name)

# Фильтрация проектов по дате создания


import datetime
#ata = datetime.datetime(year=2023, month=8, day=2).astimezone() #по умолчанию тек таймзона
#roject_filter = Project.objects.filter(date_started__gte=data)
#or p in project_filter:
#   print(p.name)

# Использование Q-класса для комбинированных условий
#
# Импортируйте модель Project.
# Напишите запрос, который позволит получить необходимые проекты:
# Реализуйте фильтрацию, которая будет проходить два условия:
# Проекты, равные или больше указанной даты
# Проекты, у которых в имени есть строка ‘TI’
# Выведите имена таких проектов.

from projects.models import Project
from django.db.models import Q
#date_ = datetime.datetime(year=2023, month=8, day=2).astimezone()
#req_proj = Project.objects.filter(Q(date_started__gte=date_) & Q(name__icontains="TI"))
#for p in req_proj:
#    print(p.name)

# Получение списка всех файлов для конкретного проекта
#from projects.models import ProjectFile
#file_list = ProjectFile.objects.filter(projects__name='TIGER')
#'# Напишите запрос, который позволит получить список всех файлов, которые привязаны к конкретному проекту. Поиск произведите по имени проекта.
#'# Выведите только пути к каждому файлу.
#for file in file_list:
#    print(file.file) # выводим пути


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

from projects.models import Tag, Project, ProjectFile, Task
from projects.choices import Statuses, Priorities

from django.db import connection, reset_queries
from time import time

reset_queries()
start = time()

status = Statuses.NEW
priority_id = Priorities.from_label("Critical").db_value

tasks = Task.objects.filter(
    Q(status=status) & Q(priority=priority_id)
)

for task in tasks:
    print(f"""{task.title=}, {task.status=}, {task.priority=}, {task.due_date=}, {task.assignee.email=}""")

stop = time()

for q in connection.queries:
    print(q.get("sql"))

print("Длина: ", len(connection.queries))
print("Врем затраченное: ", stop - start)
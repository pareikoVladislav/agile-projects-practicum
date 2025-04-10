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

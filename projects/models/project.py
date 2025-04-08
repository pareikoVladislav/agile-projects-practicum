from django.db import models

from projects.models.project_file import ProjectFile


class Project(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    files = models.ManyToManyField(ProjectFile, related_name='projects')
    date_started = models.DateField(auto_now_add=True)

    @property
    def count_of_files(self):
        return self.files.count()

    class Meta:
        ordering = ['-name']
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.name

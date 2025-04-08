from django.db import models


class ProjectFile(models.Model):
    name = models.CharField(max_length=120)
    file = models.FileField(upload_to='projects/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Project File'
        verbose_name_plural = 'Project Files'
        ordering = ['-created_at']

from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    
    def _str_self(self):
        return self.title


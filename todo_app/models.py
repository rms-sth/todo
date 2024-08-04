from django.db import models

# python manage.py makemigrations
# python manage.py migrate


class Todo(models.Model):  # PascalCase
    title = models.CharField(max_length=200)  # varchar, char

    def __str__(self): # dui ota underscore ho
        return self.title

from django.db import models

class Item(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(max_length=1000, verbose_name='Content Text')
    completed = models.BooleanField(default=False, verbose_name='Completed')
    priority = models.IntegerField(default=5, verbose_name='Priority')
    image = models.ImageField(upload_to="images/%Y/%m/%d/", blank=True, verbose_name='Images')
    time_create = models.TimeField(auto_now_add=True, verbose_name='Time create')
    time_update = models.TimeField(auto_now=True, verbose_name='Time update')
    is_published = models.BooleanField(default=True, verbose_name='Published')
    category = models.ForeignKey('Todo', on_delete=models.PROTECT, verbose_name='category')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'
        ordering = ['-time_update', 'pk']


class Todo(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='URL')
    priority = models.IntegerField(default=5, verbose_name='Priority')
    time_create = models.TimeField(auto_now_add=True, verbose_name='Time create')
    time_update = models.TimeField(auto_now=True, verbose_name='Time update')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'
        ordering = ['pk']
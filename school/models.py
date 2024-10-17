from django.db import models

from users.common import NULLABLE


class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    image = models.FileField(verbose_name='Превью', **NULLABLE)
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ('title',)


class Lesson(models.Model):
    course = models.ForeignKey(Course, related_name='lesson', on_delete=models.CASCADE)
    title = models.CharField(max_length=150, verbose_name='Название')
    image = models.FileField(verbose_name='Превью', **NULLABLE)
    description = models.TextField(verbose_name='Описание')
    url = models.URLField(**NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        ordering = ('title',)

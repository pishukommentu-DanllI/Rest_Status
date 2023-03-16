from django.db import models


class PositionJob(models.Model):
    name = models.CharField(max_length=255, verbose_name='Должность сотрудника')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'


class Employee(models.Model):
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=255, verbose_name='Отчество')
    PositionJob = models.ForeignKey(PositionJob, on_delete=models.CASCADE, verbose_name='Должность')
    login = models.CharField(max_length=100, verbose_name='Логин')
    password = models.CharField(max_length=100, verbose_name='Пароль')
    photo = models.URLField(verbose_name='Ссылка на фото')

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}. Должность {self.PositionJob}'

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class Status(models.Model):
    name = models.CharField(max_length=255, verbose_name='Статус')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Order(models.Model):
    table = models.IntegerField(verbose_name='Номер столика')
    time = models.TimeField(verbose_name='Время брони')
    cost = models.IntegerField(verbose_name='Цена')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name='Статус')
    Employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name='Работник')

    def __str__(self):
        return f'Заказ на столик {self.table} в {self.time}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['-time', 'cost']

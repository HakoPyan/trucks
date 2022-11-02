from django.db import models


class Model(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name}'


class Truck(models.Model):
    board_number = models.CharField(max_length=20)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    max_capacity = models.IntegerField()
    current_capacity = models.IntegerField()

    def __str__(self):
        return f'{self.model} {self.board_number}'

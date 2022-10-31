from django.db import models


# Create your models here.
class Truck(models.Model):
    board_number = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)
    max_capacity = models.IntegerField()
    curr_capacity = models.IntegerField()

    def __str__(self):
        return f'{self.brand} {self.board_number} has max capacity of {self.max_capacity} tons and carries ' \
               f'{self.curr_capacity} now'

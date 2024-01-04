from django.db import models


class Workout(models.Model):
    id = models.AutoField(primary_key=True)
    workout_date = models.DateTimeField(verbose_name='workout date')

    def __str__(self):
        return self.id


class Exercise(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, verbose_name='name')
    reps = models.IntegerField(verbose_name='reps')
    series = models.IntegerField(verbose_name='series')
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    muscle = models.CharField(max_length=200, verbose_name='muscle')

    def __str__(self):
        return self.name


class Sample_exercise(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, verbose_name='name')
    reps = models.IntegerField(verbose_name='reps')
    series = models.IntegerField(verbose_name='series')
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    muscle = models.CharField(max_length=200, verbose_name='muscle')

    def __str__(self):
        return self.name

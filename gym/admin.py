from django.contrib import admin
from .models import Workout, Exercise, Sample_exercise
# Register your models here.

admin.site.register(Workout)
admin.site.register(Exercise)
admin.site.register(Sample_exercise)

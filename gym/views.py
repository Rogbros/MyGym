from django.http import HttpResponse

from .models import Exercise


def index(request):
    all_exercise_list = Exercise.objects.all()
    return HttpResponse("Hello, world. You're at the gym index.")


def exercise_details(request, exercise_id):
    return HttpResponse("You are looking at the eercise with id %s" % exercise_id)

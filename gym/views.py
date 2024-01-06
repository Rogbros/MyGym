from django.http import HttpResponse
from django.template import loader

from .models import Exercise


def index(request):
    all_exercise_list = Exercise.objects.all()
    template = loader.get_template('index.html');
    context = {
        "all_exercises": all_exercise_list,
    }
    return HttpResponse(template.render(context, request))


def exercise_details(request, exercise_id):
    return HttpResponse("You are looking at the eercise with id %s" % exercise_id)


def delete_exercise(request):
    template = loader.get_template('exercise/new_exercise.html')
    return HttpResponse(template.render(request))

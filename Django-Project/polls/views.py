from django.http import HttpResponse
from django.shortcuts import render

from .models import *

# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     output = ", ".join([q.question_text for q in latest_question_list])
#     return HttpResponse(output)

# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     template = loader.get_template("polls/index.html")
#     context = {
#         "latest_question_list": latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:15]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)


def details(request, question_id): 
    # return HttpResponse("You're looking at question %s." % question_id)
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExists:
        raise Htt404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})


def result(request, question_id):
    reponse = "You're looking at hte results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("Yor're voting on question." % question_id)

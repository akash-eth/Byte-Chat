from django.shortcuts import render

from personal.models import Question

def home_screen_view(request):

    context = {}

    # list_of_value = []
    
    # list_of_value.append('first')
    # list_of_value.append('second')
    # list_of_value.append('third')

    # context['list_of_value'] = list_of_value

    questions = Question.objects.all()
    context['questions'] = questions

    return render(request, 'personal/home.html',context)

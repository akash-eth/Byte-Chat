from django.shortcuts import render


def home_screen_view(request):

    context = {}

    # list_of_value = []
    
    # list_of_value.append('first')
    # list_of_value.append('second')
    # list_of_value.append('third')

    # context['list_of_value'] = list_of_value

    # questions = Question.objects.all()
    # context['questions'] = questions


    return render(request, 'personal/home.html',context)

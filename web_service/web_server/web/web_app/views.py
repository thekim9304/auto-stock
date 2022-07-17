from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def test(request):
    data = {
        'name' : 'Hello World',
        'users' : [{'name':'아무거나', 'level' : '99'}, {'name':'아무거나', 'level' : '99'}, {'name':'아무거나', 'level' : '99'}]
    }
    
    return render(request, 'test.html', data)



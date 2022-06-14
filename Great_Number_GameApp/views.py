from django import views
from django.shortcuts import render, redirect
import random


def index(request):
    if ('randomnum' in request.session):
        pass
    else:
        request.session['randomnum'] = random.randint(1, 100)
    return render(request, "index.html")


def guess(request):
    color = ''
    message = ''
    _input= int(request.POST['guess'])
    _ran =request.session['randomnum']
    if(_ran == _input):
        color = 'green'
        message = f"{_ran} was the number!"
    else:
        color = 'red'
        if(_ran < _input):
            message = 'Too High!'
        else:
            message = 'Too Low!'
    context = {
        'color': color,
        'message': message
    }
    return render(request, "index.html", context)


def destroy (request):
    del request.session['randomnum']
    return redirect('/')

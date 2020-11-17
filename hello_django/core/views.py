from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request, nome, idade):
    return HttpResponse(f'<h1>Hello, {nome}. Você tem {idade} anos.</h1>')

def soma(request, param1, param2):
    return HttpResponse(f'<h1>Soma: {param1} + {param2} = {param1+param2}</h1>')

def sub(request, param1, param2):
    return HttpResponse(f'<h1>Subtração: {param1} - {param2} = {param1-param2}</h1>')

def mul(request, param1, param2):
    return HttpResponse(f'<h1>Multiplicação: {param1} x {param2} = {param1*param2}</h1>')

def div(request, param1, param2):
    return HttpResponse(f'<h1>Divisão: {param1} / {param2} = {param1/param2}</h1>')
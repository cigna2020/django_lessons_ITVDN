from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from . import forms
from django.core.mail import send_mail
from . import models
from django.views import generic
from django.shortcuts import render

# Create your views here.


def search_form(request):
    return render(request, 'search_form.html', {})

def search(request):
    if request.method == 'GET':
        if 'q' in request.GET:
            return HttpResponse('You want to find %s' % request.GET['q'])
        else:
            return HttpResponse('You have sent the empty form!')

def test_view(request):
    # return HttpResponse('Welcome to %s' % request.path)
    # return HttpResponse('host is %s' % request.get_host())
    # return HttpResponse('The full path is %s' % request.get_full_path())
    return HttpResponse('It is secured %s' % request.is_secure())

def file_input(request):
    name = request.POST['name']
    surname = request.POST['surname']
    birth = request.POST['birth']
    gender = request.POST['gender']
    some_file = open('some.txt', 'w')
    some_file.write('Имя:' + name + '\n')
    some_file.write('Фамилия:' + surname + '\n')
    some_file.write('Дата рождения:' + birth + '\n')
    some_file.write('Пол:' + gender + '\n')
    some_file.close()
    return HttpResponse('Your data were successfully saved!')


def form(request):
    form_for_author1 = forms.AuthorOneForm  #подключение форм, созданных в forms.py
    form_for_atrticle = forms.ArticleForm
    form_contact = forms.ContactForm
    context = {
        'form_for_author1': form_for_author1,
        'form_for_atrticle': form_for_atrticle,
        'form_contact': form_contact
    }
    return render(request, 'form.html', context)


def author_add(request):
    form = forms.AuthorOneForm(request.POST)
    result = 'Автор успешно добавлен %s' %request.path
    if request.method == 'POST':
        if form.is_valid():
            data = form.cleaned_data
            form.save()
            print(data['name'])
            return HttpResponse('Автор добавлен %s' %request.path)

def add_article():
    pass



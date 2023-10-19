from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from blog.models import UserModel


def index(request):
    return render(request,'index.html')

@csrf_exempt
def reg(request):    #Регистрация пользователя
    if request.method == 'POST':
        # обработка POST запроса
        l = request.POST['login']
        p = request.POST['pas']
        e = request.POST['email']
        n = UserModel()
        arrlog = []
        arrpas = []
        for i in UserModel.objects.all(): #прохождение по всме записям модели UserModel
            arrlog.append(i.log)  #Добавление логинов в список
            arrpas.append(i.pas)  #Добавление паролей в список
        if l in arrlog:    #Если такрй логин есть, то ошибка!
            return render(request, 'Error.html')
        n.log = l  #Если такого логина нет, то добавляем его в модель
        n.pas = p
        n.email = e
        n.save()
        #return render(request, 'New.html') # и отправляем на новую страницу
        return redirect(f'/?hello=Helloy, {l}')   #передаем в адресную сторку
    return render(request, 'Autorisation.html')

def page_auth(request):
    return render(request, 'Autorisation.html')

@csrf_exempt
def auth(request):
    if request.method == 'POST':
        l = request.POST['login']
        p = request.POST['pas']
        diclog = dict()

        for i in UserModel.objects.all():
            diclog[i.log] = i.pas

        if l in diclog.keys() and p == diclog[l]:
            return redirect(f'/?hello=Helloy, {l}')

        else:
            return render(request, 'Error_aut.html', {'x':'Ошибка!'})

def page_reg(request):
    return render(request, 'Registration.html')

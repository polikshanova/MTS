from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from .models import Profile
from shopMTS.models import Product
from django.views.generic import DetailView
from random import choice

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Создан аккаунт {username}!')
            user = User.objects.get(username=username)
            login(request, user)
            return redirect('/')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'users/register.html')

def installment(request,pk):
    form = {}
    form['check'] = 'all'
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        num = request.POST['persnumber']
        tel = request.POST['telnumber']
        if (num == profile.persnumber)and(tel==profile.telnumber):
            form['checknum']=True
            msg = [
                'Вам одобрено с первоначальным платежом 50р. ',
                'Отказ',
                'Одобрено на сумму до 5000р.'
            ]
            form['answer'] = choice(msg)


        else:
            form['checknum'] = False
            form['check'] = ''


    product = Product.objects.get(pk=pk)
    form['profile']=profile
    form['product']=product

    return render(request, 'users/installment.html', form)







class Installment(DetailView):
    model = Product
    template_name = "installment.html"
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cur_user = self.request.user
        prof = Profile.objects.get(user=cur_user)
        # num = self.request.POST['persnumber']
        # context['persnumber']=num
        return context

    # def post(self, request, *args, **kwargs):
    #     self.object = self.get_object()

from django.shortcuts import render, redirect
from django.views.generic import *
from django.http import *
from .models import ToDoInfo
from django.contrib import messages
from .forms import AddRecordForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



class home(TemplateView, LoginRequiredMixin):
    def get(self, request):
        return render(request, 'home.html')


class MainToDoList(View, LoginRequiredMixin):
    def get(self,request):
        if request.user.is_authenticated:
            full_list = ToDoInfo.objects.all() 
            contex = {
                'full_list':full_list
            }
            return render(request, 'main-todolist.html', context=contex)

        else:
            messages.success(request, 'You Need To Login First',  extra_tags='danger')
            return redirect('login')
        
    def post(self,request):
        AddToList = request.POST['add-to-list']
        add = ToDoInfo.objects.create(title=AddToList)
        return redirect('main-list')


class DeleteRow(DeleteView, LoginRequiredMixin):
    def get(self, request, pk):
        if request.user.is_authenticated:
            delete_recored = ToDoInfo.objects.get(id=pk)
            delete_recored.delete()
            messages.success(request,'Delete The Item')
            return redirect('main-list')

class UpdateRow(UpdateView, LoginRequiredMixin):
    def get(self, request, pk):
            current_ToToDoInfo =ToDoInfo.objects.get(id=pk)
            form = AddRecordForm(request.POST or None ,instance=current_ToToDoInfo)
            context = {
                'form':form
            }
            return render(request, template_name='update.html',context=context )

    def post(self, request, pk,):
        current_ToToDoInfo =ToDoInfo.objects.get(id=pk)
        form = AddRecordForm(request.POST or None ,instance=current_ToToDoInfo)
        context = {
            'form':form
        }
        if form.is_valid():
            form.save()
            messages.success(request, f'Your Item Is Updated'.title())
            return redirect('main-list')
        

class Login(TemplateView):
    def get(self, request):
        return render(request, 'login.html')
    
    def post(self, request):
        username = request.POST['username']
        psw = request.POST['password']

        user = authenticate(request, username=username, password=psw)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login Sccuffule')
            return redirect('main-list')
        else:
            messages.success(request, 'Invaild Email Or Password',  extra_tags='danger')
            return redirect('login')


class Logout(TemplateView):
    def get(self, request):
        logout(request)
        messages.success(request, "You Have Been Logged Out")
        return redirect('home')
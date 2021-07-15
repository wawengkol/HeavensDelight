from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib import messages
from .forms import CreateUserForm

# Create your views here.
def home(request):
    return render(request, 'Index.html')

def dashboardView(request):
    return render(request, 'dashboard.html')

def indexmainView(request):
    return render(request, 'indexmain.html')


def LoginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()

            return redirect('dashboard')
    else:
        form = AuthenticationForm()

    return render(request,'LOGIN.html',{'form':form})


def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            return redirect('login_url')
    else:
        form = CreateUserForm()
    return render(request, 'REGISTER.html',{'form':form})

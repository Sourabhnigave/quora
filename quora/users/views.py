from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User 
from .forms import CustomUserCreationForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required



def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful! You can now log in.")
            return redirect('login')  # Redirect to login page
        else:
            for field_errors in form.errors.values():
                for error in field_errors:
                    messages.error(request, error)
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email') 
        password = request.POST.get('password')

        if email and password:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                user = None

            if user and user.check_password(password):
                login(request, user)  
                return redirect('home')  
            else:
                messages.error(request, 'Invalid email or password.')  
        else:
            messages.error(request, 'Both email and password are required.')
    
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')
def home(request):
    return render(request, 'home.html')  
@login_required
def user_list(request):
    users = User.objects.all()
    print(users)
    return render(request, 'CCPLAPP/user_list.html', {'users': users})
@login_required
def user_form(request, id=None):
    if id:
        user = get_object_or_404(User, id=id)
    else:
        user = None

    print("Raw POST Data:", request.POST)

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            print("User saved successfully.")
            return redirect('user-list')
        else:
            print("Form errors:", form.errors) 
    else:
        form = CustomUserCreationForm(instance=user)

    return render(request, 'CCPLAPP/user_form.html', {'form': form})



@login_required
def user_delete(request, id):
    if not request.user.is_authenticated:
        return redirect('login')

    user = get_object_or_404(User, id=id)

    if request.method == "POST":
        user.delete()
        return redirect('user-list')

    return render(request, 'CCPLAPP/user_confirm_delete.html', {'user': user})
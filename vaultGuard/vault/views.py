from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .forms import SignUpForm, SignInForm, AddEntryForm
from .models import Entry
import random
import string
import logging

logger = logging.getLogger(__name__)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        logger.info(f"Form data: {request.POST}")
        if form.is_valid():
            user = form.save()
            messages.success(request, "You have successfully signed up! Please sign in.")
            logger.info("User created successfully")
            return redirect('signin')
        else:
            logger.error(f"Form errors: {form.errors}")
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You have successfully signed in!")
                return redirect('home')
            else:
                messages.error(request, "Invalid email or password.")
    else:
        form = SignInForm()
    return render(request, 'accounts/signin.html', {'form': form})

@login_required
def home(request):
    entries = Entry.objects.filter(user=request.user).order_by('title')
    return render(request, 'vault/home.html', {'entries': entries})

@login_required
def ai_assistance(request):
    return render(request, 'vault/ai_assistance.html')

@login_required
def generator(request):
    return render(request, 'vault/generator.html')

@login_required
def add_entry(request):
    if request.method == 'POST':
        form = AddEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            return redirect('home')
    else:
        form = AddEntryForm()
    return render(request, 'vault/add_entry.html', {'form': form})

@login_required
def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id, user=request.user)
    if request.method == 'POST':
        form = AddEntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddEntryForm(instance=entry)
    return render(request, 'vault/edit_entry.html', {'form': form, 'entry': entry})

def user_logout(request):
    logout(request)
    messages.success(request, "You have been successfully logged out.")
    return redirect('signin')

@login_required
def generate_password(request):
    length = 12
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return JsonResponse({'password': password})


from django.shortcuts import render, redirect
from .forms import UserRegistraionForm, UserConfirmationForm
from django.contrib.auth import login

def signup(request):
    form = UserRegistraionForm
    if request.method == "POST": #
        form = UserConfirmationForm(request.POST)

        if form.is_valid():
            login(request, form.get_user())
            return redirect("blog:root")

    return render(request, 'signup.html',)

def signin(request):
    form = UserConfirmationForm
    return render(request, 'signin.html',{"form":form})
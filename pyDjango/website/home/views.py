from datetime import datetime
from django.shortcuts import render,redirect
from .models import User
from .forms import UserForm

def index(request):
    current_datetime = datetime.now()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # Save the data to the database
            User.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email']
            )
            return redirect('display_users')
    else:
        form = UserForm()
    context = {
        'form': form,
        'current_datetime': current_datetime,
    }
    return render(request,"index.html",context)


def display_users(request):
    users = User.objects.all()
    return render(request, 'display_users.html', {'users': users})



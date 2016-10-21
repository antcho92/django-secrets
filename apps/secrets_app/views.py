from django.shortcuts import render, redirect
from ..login_reg_app.models import User
from .models import Secret, Like
from django.contrib import messages
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
    if 'user_id' in request.session:
        secrets = Secret.objects.all().order_by('updated_at')
        context = {
            'secrets': secrets
        }
        return render(request, 'secrets_app/index.html', context)
    else:
        return redirect(reverse('users:index'))

def add(request):
    if request.method == 'POST':
        print("adding secret")
        user = User.objects.get(id=request.session['user_id'])
        validation = Secret.objects.add_secret(request.POST, user)
        if not validation[0]:
            messages.error(request, validation[1])
        else:
            print('passed validations')
            messages.success(request, "Secret has been added successfully")
    else:
        messages.error("Something went wrong. Try again")
    return redirect(reverse('secrets:index'))
def delete(request, id):
    print("deleting secret", id)
    validation = Secret.objects.delete_secret(id, request.session['user_id'])
    if validation[0]:
        messages.success(request, validation[1])
    else:
        messages.error(request, valdiation[1])
    return redirect(reverse('secrets:index'))
def like(request, secret_id):
    validation = Like.objects.add_like(secret_id, request.session['user_id'])
    if validation[0]:
        messages.success(request, validation[1])
    else:
        messages.error(request, validation[1])
    return redirect(reverse('secrets:index'))

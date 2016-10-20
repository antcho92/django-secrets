from django.shortcuts import render, redirect
from ..login_reg_app.models import User
from django.contrib import messages
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
    return render(request, 'secrets_app/index.html')

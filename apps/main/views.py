from django.shortcuts import render
from django.db import transaction
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404


def main(request):
    if request.user.is_authenticated:
        return render(request, "index.html")
    else:
        return redirect('/login/')

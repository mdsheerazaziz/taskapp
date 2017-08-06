# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from sodingassignment.taskapp.task_handler import new_task, get_all_task, remove_task, get_task, save_modified_task


def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
    else:
        return None


def logout_view(request):
    logout(request)


def home(request):
    if request.user.is_authenticated():
        tasks = get_all_task(request.user)
        return render(request, "index.html", {"tasks": tasks})
    else:
        return redirect("/login")


def add_task_page(request):
    return render(request, "addTask.html")


def create_task(request):
    new_task(request.POST, request.user)
    return redirect("/")


def edit_task(request):
    task = get_task(request.GET.get("id"), request.user)
    if task:
        return render(request, "editTask.html", {"task": task})
    else:
        return redirect("/")


def modify_task(request):
    save_modified_task(request.POST, request.user)
    return redirect("/")


def delete_task(request):
    remove_task(request.GET.get("id"), request.user)
    return redirect("/")

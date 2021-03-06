from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from django.urls import reverse_lazy
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from django.contrib.auth.decorators import login_required

from django.contrib import messages
from django.http import JsonResponse

from . import forms
from . import models

class SignUpView(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'sudoku_app/signup.html'


class IndexView(TemplateView):
    template_name = 'index.html'


class sudoku_appIndexView(TemplateView):
    template_name = 'sudoku_app/base.html'


def index(request):
    return HttpResponse("hi there")


class HealthView(View):
    """Health view."""

    def get(self, request, *args, **kwargs):
        """Get method."""
        from django.db import connections
        from django.db.utils import OperationalError
        db_conn = connections['default']
        try:
            db_conn.cursor()
        except OperationalError:
            connected = False
        else:
            connected = True
        data = {'db_connected': connected}
        return JsonResponse(data)

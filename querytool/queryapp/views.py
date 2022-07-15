from .models import Cui, Tui, Query
from django.shortcuts import render
from django.views import generic
from datetime import date
from django.http import Http404
from django.contrib.auth.decorators import login_required
from queryapp.forms import QueryForm
from django import forms
@login_required
def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    num_queries=Query.objects.all().count()
    return render(
        request,
        'index.html',
        context={'num_queries':num_queries},
    )


class QueryListView(generic.ListView):
    model = Query

def query_detail_view(request,pk):
    try:
        query_id=Query.objects.get(pk=pk)
    except Query.DoesNotExist:
        raise Http404("Book does not exist")
    for i in query_id.tui.all():
        print(i)
    return render(
        request,
        'queryapp/query_detail.html',
        context={'query':query_id, 'form':QueryForm}
    )

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class QueryCreate(CreateView):
    # model = Query
    template_name = 'queryapp/query_form.html'
    form_class = QueryForm
    # fields = '__all__'
    # initial={'tui':'T184', 'name':'HUUUI'}
    # name = forms.CharField(initial='какое-то имя', widget=forms.Textarea,
    #                        help_text="Введите назввание запроса. Его потом проще будет найти)")
    # tui = forms.ModelMultipleChoiceField(
    #     queryset=Tui.objects.all(),
    #     widget=forms.CheckboxSelectMultiple,
    #     required=False
    # )
    # сui = forms.HiddenInput()
    # link = forms.ModelChoiceField(queryset=Tui.objects.all())
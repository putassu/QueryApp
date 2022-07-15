# from dal import autocomplete
from .models import Cui, Tui, Query
from django import forms
from django.core.exceptions import ValidationError
import datetime

# class Form(forms.ModelForm):
#     diagnosis = forms.ModelChoiceField(
#         queryset=Diagnosis.objects.all(),
#         widget=autocomplete.ModelSelect2(url='catalog:diagnosis-autocomplete')
#     )
#
#     class Meta:
#         model = Case
#         fields = ('__all__')
#
# class Form2(forms.ModelForm):
#     services = forms.ModelChoiceField(
#         queryset=Service.objects.all(),
#         widget=autocomplete.ModelSelect2(url='services-autocomplete')
#     )
#
#     class Meta:
#         model = Visit
#         fields = ('__all__')
#

# class QueryForm(forms.ModelForm):
#     name = forms.CharField(initial = 'какое-то имя', widget=forms.Textarea, help_text="Введите назввание запроса. Его потом проще будет найти)")
#
#     class Meta:
#         model = Query
#         fields = '__all__'
#         exclude = ['id',]
#         labels = {'name': 'Название запроса', 'cui': 'CUI', 'tui': 'TUI', 'link': 'Тип связи',
#                   'figure': 'Эвристический подход к рассчету коэффициента кластеризации',
#                   'cc_1': 'Коэффициент кластеризации 1', 'max_embeddings': 'Максимальное количество эмбеддингов',
#                   'join': 'Тип объединения', 'range':'Ранжировать по', 'level':'Уровень подграфа', 'lang':'Язык'}
#         widgets = {'name':forms.Textarea}
#         initials = {'figure':0, 'cc_1':2, 'Ранжировать по':0}

class QueryForm(forms.ModelForm):
    name = forms.CharField(initial = 'какое-то имя', widget=forms.Textarea, help_text="Введите назввание запроса. Его потом проще будет найти)")
    tui =forms.ModelMultipleChoiceField(
        queryset=Tui.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False, initial=[0,1,2,3]
    )
    # cui_1 = forms.TypedMultipleChoiceField(
    #     queryset=Cui.objects.all(),
    #     required=False
    # )
    сui = forms.HiddenInput()
    link = forms.ModelChoiceField(queryset=Tui.objects.all())
    class Meta:
        model = Query
        fields = '__all__'
    # figure =
    # max_embeddings =
    # level =
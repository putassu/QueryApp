from django.db import models
from django.urls import reverse, reverse_lazy
import uuid
import datetime
from django.contrib.auth.models import User
from django.utils.html import format_html
from django import forms
app_name = 'queryapp'
class Cui(models.Model):
    """
    Model representing a concept
    """
    cui = models.CharField('СUI', primary_key=True, max_length=15, blank=True, help_text='Номер концепта')
    cui_ru = models.CharField("Название концепта на русском", max_length=100)
    cui_en = models.CharField("Название концепта на английском", max_length=100)
    class Meta:
        ordering = ["cui_ru"]
        verbose_name_plural = 'Концепты'
        verbose_name = 'концепт'
    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s %s' % (self.cui, self.cui_ru)


    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('queryapp:сui-detail', args=[str(self.id)])


# class Link(models.Model):
#     """
#     Model representing a patient
#     """
#     id = models.AutoField(primary_key=True,help_text="ID")
#     # link = models.CharField('Тип связи', max_length=5, blank=True, help_text='Введите тип связи')
#
#     # date = models.DateField("Дата изменения", default=datetime.date.today)
#     class Meta:
#         ordering = ["id"]
#         verbose_name_plural = 'Типы связей'
#         verbose_name = 'тип связи'
#     def __str__(self):
#         """
#         String for representing the Model object.
#         """
#         return '%s' % (self.id)
#
#
#     def get_absolute_url(self):
#         """
#         Returns the url to access a particular book instance.
#         """
#         return reverse('queryapp:link-detail', args=[str(self.id)])


class Tui(models.Model):
    """
    Model representing a patient
    """
    id = models.AutoField(primary_key=True,help_text="ID")
    tui = models.CharField('TUI', max_length=5, blank=True, help_text='Семантическая группа')
    tui_name = models.CharField('Название семантической группы', max_length=50, blank=True, help_text='Название семантической группы')

    class Meta:
        ordering = ["tui"]
        verbose_name_plural = 'Семантические группы'
        verbose_name = 'семантическая группа'
    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s' % (self.tui)


    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('queryapp:tui-detail', args=[str(self.id)])


class Query(models.Model):
    id = models.AutoField(primary_key=True,help_text="ID")
    name = models.CharField('Название запроса', max_length=50, blank=True, help_text='Дайте своему запросу имя. Потом легче найти будет)')
    cui = models.ForeignKey(Cui,null=True, on_delete=models.SET_NULL)
    tui = models.ManyToManyField(Tui)
    AQ = models.BooleanField("AQ")
    CHD = models.BooleanField("CHD")
    PAR = models.BooleanField("PAR")
    RB = models.BooleanField("RB")
    RL = models.BooleanField("RL")
    RO = models.BooleanField("RO")
    RQ = models.BooleanField("RQ")
    SIB = models.BooleanField("SIB")
    SM = models.BooleanField("SM")
    SMP = models.BooleanField("SMP")
    SY = models.BooleanField("SY")
    QB = models.BooleanField("QB")
    FIG = [(0, 'Треугольник (2112)'),
           (1, 'Треугольник (1221)'),
           (2, 'Ромб (01210)')]
    figure = models.IntegerField('Фильтр', max_length=5, choices=FIG, blank=True, help_text='Эвристический подход к расчету метрик связности')
    cc_1 = models.FloatField('Коэффициент кластеризации 1')
    cc_2 = models.FloatField('Коэффициент кластеризации 2')
    cc_3= models.FloatField('Коэффициент кластеризации 3')
    max_embeddings = models.IntegerField('Максимальное количество соседей по косинусной мере')
    JOIN = [(0,'left'),
            (1,'inner'),
            (2,'right')]
    join = models.IntegerField('Тип объединения', max_length=5, choices=JOIN, blank=True, help_text='Объединить концепты с наибольшими коэффициентами кластеризации и косинусной меры')
    RANGE = [(0,'Среднее арифметическое'),
             (1,'Среднее гармоническое'),
             (2,'И т д')]
    range = models.IntegerField('Ранжировать по', max_length=5, choices=RANGE, blank=True, help_text='Эвристический подход к расчету метрик связности')

    LEVEL = [(1, 'онтология'),
           (2, 'симптомы'),
           (3, 'расширенный список симптомов'),
             (4,'глобальный список')]
    level = models.IntegerField('Уровень подграфа', max_length=5, choices=LEVEL, blank=True,
                              help_text='Уровни подграфа')
    LANG = [(0,'RUS'),
            (1,'ENG'),
            (2,'RUS+ENG')]
    lang = models.IntegerField('Язык', max_length=5, choices=LANG, blank=True,
                              help_text='Языки')
    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s %s %s %s %s %s %s' % (self.figure,self.cc_1,self.max_embeddings,
                                             self.join,self.range,self.level,self.lang)


    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('query-detail', args=[str(self.id)])



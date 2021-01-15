# -*- coding: utf-8 -*-
from django.views.generic import ListView
from django.views.generic.base import ContextMixin
from django.views.generic.edit import FormMixin


class TitleMixin:
    title = ''

    def get_title(self):
        return self.title

    def get_context_data(self, **kwargs):
        c = super(TitleMixin, self).get_context_data(**kwargs)

        title = self.get_title()
        if title:
            c['title'] = title

        return c

class BreadcrumbsMixin(ContextMixin):

    def get_breadcrumbs(self):
        return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breadcrumbs'] = self.get_breadcrumbs()
        return context


class FilterView(FormMixin, ListView):
    model = None
    form_class = None
    template_name = None
    paginate_by = None
    title = u'Поиск'

    def filter(self, queryset):
        return queryset

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['data'] = self.request.GET or None
        return kwargs

    def get_queryset(self):
        self.form = self.get_form()
        if self.form.is_valid():
            queryset = super(FilterView, self).get_queryset()
            queryset = self.filter(queryset)
        else:
            queryset = super(FilterView, self).get_queryset()

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form
        return context
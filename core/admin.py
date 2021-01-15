from django.contrib import admin


# Register your models here.
from core.models import *


class StudentInline(admin.TabularInline):
    model = Student


class AnswerInline(admin.TabularInline):
    model = Answer


class TestStudentInline(admin.TabularInline):
    model = TestStudent


class QuestionInline(admin.TabularInline):
    model = Question


class StudentAnswerInline(admin.TabularInline):
    model = StudentAnswer


class ResultInline(admin.TabularInline):
    model = Result


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'patronymic', 'surname', 'user', 'group')
    list_filter = ('name', 'patronymic', 'surname', 'user', 'group')
    fields = ('name', 'patronymic', 'surname', 'user', 'group')
    raw_id_fields = ('user', )
    # inlines = [StudentInline]
    ordering = ('name', 'patronymic', 'surname', 'user', 'group')


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('name', 'question', 'is_correct')
    list_filter = ('name', 'question', 'is_correct')
    fields = ('name', 'question', 'is_correct')
    raw_id_fields = ('question', )
    ordering = ('question', 'is_correct')



@admin.register(TestStudent)
class TestStudentAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    fields = ('name',)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('name', 'test')
    list_filter = ('name', 'test')
    fields = ('name', 'test')
    raw_id_fields = ('test', )
    ordering = ('name', 'test')


@admin.register(StudentAnswer)
class StudentAnswerAdmin(admin.ModelAdmin):
    list_display = ('student', 'answer', 'dc')
    list_filter = ('student', 'answer', 'dc')
    fields = ('student', 'answer')
    # inlines = [StudentInline]
    raw_id_fields = ('student', 'answer')
    ordering = ('student', 'answer')


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('student', 'test', 'dc', 'count_true', 'count_false')
    list_filter = ('student', 'test', 'dc', 'count_true', 'count_false')
    fields = ('student', 'test', 'count_true', 'count_false')
    raw_id_fields = ('student', 'test')
    ordering = ('student', 'test', 'dc', 'count_true', 'count_false')











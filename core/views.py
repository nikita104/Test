from django.shortcuts import render
# from speechd_config.config import question

from core.models import *

# Create your views here.
from django.views.generic import TemplateView

from lib.generic_mixin import BreadcrumbsMixin



class Index(BreadcrumbsMixin, TemplateView):
    template_name = 'index.hhttps://github.com/nikita104/Test.gittml'

    def get_breadcrumbs(self):
        return [
            ('Заявки со склада', ''),
            ('Редактирование заявки', ''),
        ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['student'] = Student.objects.get(user=self.request.user)
        return context


def tests(request):
    tests = TestStudent.objects.all()

    context = {
        'tests': tests,
    }
    return render(request, 'tests.html', context)


def test_student(request, id):
    test = TestStudent.objects.get(id=id)
    user, _ = Student.objects.get_or_create(user_id=request.user.id, defaults={'user_id': id})
    result = None
    results = {}
    if request.POST:
        student_answer_ids = [int(answer_id) for answer_id in request.POST if answer_id.isdigit()]
        questions = Question.objects.filter(test=1)
        for question in questions:
            results[question.id] = True
            positive_answers = Answer.objects.filter(is_correct=True, question=question)
            for p_a in positive_answers:
                if p_a.id in student_answer_ids:
                    pass
                else:
                    results[question.id] = False
        count_true = len([v for v in results.values() if v is True])
        count_false = len([v for v in results.values() if v is False])
        result = Result.objects.create(student=user, test=test, count_true=count_true, count_false=count_false)
    context = {
        'test': test,
        'result': result,
    }
    return render(request, 'test_student.html', context)


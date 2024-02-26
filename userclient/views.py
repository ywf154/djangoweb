from django.forms import ModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from userclient.models import Course


def login(request):
    return render(request, 'login.html')


def layout(request):
    return render(request, 'layout.html')


def course_list(request):
    # 1.获取数据库中所有的用户信息
    data_list = Course.objects.all()
    return render(request, 'course_list.html', {"data_list":data_list})


class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'  # 或者指定要包含的特定字段






def vfor(request):
    return render(request, 'billing.html')


def course_add(request):
    if request.method == 'GET':
        return render(request, 'course_add.html')
    course_id = request.POST.get('course_id')
    credit = request.POST.get('credit')
    classifier = request.POST.get('classifier')
    attribute = request.POST.get('attribute')
    semester = request.POST.get('semester')
    Course.objects.create(
        course_id=course_id,
        credit=credit,
        classifier=classifier,
        attribute=attribute,
        semester=semester)
    return redirect('/course/list/')








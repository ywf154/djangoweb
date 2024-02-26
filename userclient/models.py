from django.core.validators import RegexValidator
from django.db import models
import datetime
from django.db.models import ForeignKey

gender_choices = ((1, "男"), (2, "女"))
yes_no = ((1, "是"), (2, "否"))
classifier_choices = (
    ('A', "纯理论课"), ('B', "理论+实践"), ('C', "纯实践课"),
)
attribute_choices = (
    (1, '通识性课程'), (1, '公共选修课'), (3, '专业基础课'), (4, "专业必修课"), (5, "专业选修课"), (6, '素质拓展课'),
    (7, '独立实践环节'),
)


class Department(models.Model):
    __table__ = '学院信息表'
    department_id = models.IntegerField(verbose_name="学院编号", unique=True, primary_key=True)
    departmentName = models.CharField(verbose_name='学院名称', max_length=100, unique=True)

    # 为admin界面设计
    class Meta:
        verbose_name = '学院信息表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.departmentName


class Major(models.Model):
    __table__ = '专业库'
    major_id = models.IntegerField(verbose_name="专业代号", unique=True, primary_key=True)
    majorName = models.CharField(verbose_name='专业名称', max_length=100, unique=True)
    department = models.ForeignKey(to='Department', to_field='departmentName', verbose_name="专业所属学院",
                                   on_delete=models.CASCADE)

    class Meta:
        verbose_name = '专业库'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.majorName


class Student(models.Model):
    __table__ = '学生库'
    student_id = models.IntegerField(verbose_name="学号", primary_key=True)
    name = models.CharField(verbose_name="学生姓名", max_length=10, unique=True)
    idNumber = models.CharField(verbose_name="身份证号码", unique=True, max_length=18)
    gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choices)
    password = models.CharField(verbose_name="密码", max_length=50)

    class Meta:
        verbose_name = '学生库'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    @property
    def age(self):
        today = datetime.date.today()
        age = today.year - int(self.idNumber[6:10])
        return age

    phone = models.CharField(verbose_name="手机号", max_length=11, unique=True)
    major = models.ForeignKey(to='Major', to_field='majorName', verbose_name="所在专业", on_delete=models.CASCADE)
    department = models.ForeignKey(to='Department', to_field='departmentName', verbose_name="所在学院",
                                   on_delete=models.CASCADE)
    ethnicity = models.CharField(verbose_name="民族", default='汉族', max_length=10)
    enterYear = models.DateField(verbose_name='入学年份')
    group = ForeignKey(to='Group', to_field='groupName', verbose_name="所在班级", on_delete=models.CASCADE)


class Teacher(models.Model):
    __table__ = '教师库'
    teacher_id = models.IntegerField(verbose_name="教师工号", primary_key=True)
    name = models.CharField(verbose_name="教师姓名", max_length=10, unique=True)
    gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choices)
    password = models.CharField(verbose_name="密码", max_length=50)
    age = models.IntegerField(verbose_name="年龄", )
    phone = models.CharField(verbose_name="手机号", max_length=11, unique=True)
    department = models.ForeignKey(to='Department', to_field='departmentName', verbose_name="学院（部门）",
                                   on_delete=models.CASCADE)

    class Meta:
        verbose_name = '教师库'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Group(models.Model):
    __table__ = '班级库'
    groupName = models.CharField(verbose_name="班级", max_length=20, primary_key=True)
    grade = models.SmallIntegerField(verbose_name="班级所属年级")
    major = models.ForeignKey(to='Major', to_field='majorName', verbose_name="班级所在专业", on_delete=models.CASCADE)
    course = models.ForeignKey(to='Course', to_field='courseName', verbose_name="分配课程", on_delete=models.CASCADE)

    class Meta:
        verbose_name = '班级库'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.groupName


class Course(models.Model):
    __table__ = '课程库'
    course_id = models.IntegerField(verbose_name="课程编号", primary_key=True)
    courseName = models.CharField(max_length=100, verbose_name="课程名称", unique=True)
    credit = models.IntegerField(verbose_name="学分")
    classifier = models.CharField(verbose_name="课程类别", max_length=1)
    attribute = models.SmallIntegerField(verbose_name="课程属性")
    semester = models.CharField(verbose_name="课程所属学期", max_length=10, validators=[
        RegexValidator(
            regex=r'第\s*(\d+)\s*学期',
            message='请填入第几学期'
        )
    ])

    @property
    def hours(self):
        return self.credit * 16

    class Meta:
        verbose_name = '课程库'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.courseName

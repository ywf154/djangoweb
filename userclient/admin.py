from django.contrib import admin
from userclient.models import *

admin.site.register(Department)
admin.site.register(Major)
admin.site.register(Group)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Course)

admin.site.site_header = '学习管理系统'

from django.contrib import admin
from .models import Problem, Submission, TestCases

# Register your models here.
admin.site.register(Problem)
admin.site.register(Submission)
admin.site.register(TestCases)
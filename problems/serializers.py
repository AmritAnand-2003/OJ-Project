from rest_framework import serializers
from .models import Problem, TestCases, Submission, RunCode


class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = "__all__"

class AddProblemSerializer(serializers.ModelSerializer):
    # title = serializers.CharField(required=True)
    # description = serializers.CharField(required=True)
    # difficulty = serializers.CharField()
    class Meta:
        model = Problem
        fields = "__all__"

class AddTestCaseSeriallzer(serializers.ModelSerializer):
    class Meta:
        model = TestCases
        fields = "__all__"

class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = ['problem', 'language', 'code']

class RunCodeSerializer(serializers.ModelSerializer):
    # code = serializers.CharField()
    # language = serializers.CharField()
    # input_data = serializers.CharField()
    class Meta:
        model = RunCode
        fields = ['code', 'language', 'input_data']
        # extra_kwargs = {
        #     'input_data': {'required': False, 'allow_blank': True}
        # }
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Problem, TestCases, Submission
from .serializers import ProblemSerializer, AddProblemSerializer, AddTestCaseSeriallzer, SubmissionSerializer, RunCodeSerializer
from rest_framework.response import Response
from .judge.compiler import Compiler
from .judge.judge import Judge
compiler = Compiler()
judge = Judge()
# Create your views here.

class AddProblemAPIView(APIView):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer

    # authentication_classes = [JWTAuthentication]  # Use JWT authentication
    # permission_classes = [IsAuthenticated]  # Require authentication to access the API

    def post(self, request):
        serializer = AddProblemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            title = serializer.data["title"]
            description = serializer.data["description"]
            difficulty = serializer.data["difficulty"]
            problem = Problem.objects.create(title=title, description=description, difficulty=difficulty)
            problem.save()
            print("saved")
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    def get(self, request):
        problems = Problem.objects.filter()
        serializer = ProblemSerializer(problems, many=True)
        return Response(serializer.data, status=201)

class ProblemListAPIView(APIView):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer

    # authentication_classes = [JWTAuthentication]  # Use JWT authentication
    # permission_classes = [IsAuthenticated]  # Require authentication to access the API

    def get(self, request):
        problems = Problem.objects.all()
        serializer = ProblemSerializer(problems, many=True)
        return Response(serializer.data)
    

    
class ProblemDetailAPIView(APIView):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer
    lookup_field = "code"

    authentication_classes = [JWTAuthentication]  # Use JWT authentication
    permission_classes = [IsAuthenticated]

class AddTestCaseAPIView(APIView):
    # authentication_classes = [JWTAuthentication]  # Use JWT authentication
    # permission_classes = [IsAuthenticated]
    serializer_class = AddTestCaseSeriallzer

    def post(self, request):
        serializer = AddTestCaseSeriallzer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # problemid = serializer.data["problem"]
            # input_data = serializer.data["input_data"]
            # output_data = serializer.data["output_data"]
            # problem = Problem.objects.get(id=problemid)
            # testcase = TestCases.objects.create(problem=problem, input_data=input_data, output_data=output_data)
            # testcase.save()
            # print("saved")
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)



class SubmitCodeAPIView(APIView):
    # authentication_classes = [JWTAuthentication]  # Use JWT authentication
    # permission_classes = [IsAuthenticated]
    serializer_class = SubmissionSerializer
    def post(self, request):
        print(request.data)
        serializer = SubmissionSerializer(data=request.data)
        # breakpoint()
        print("serializer: ", serializer)
        if serializer.is_valid():
            print("serializer is valid")
            # serializer.save()

            language = serializer.data["language"]
            code = serializer.data["code"]
            problem_id = serializer.data["problem"]
            verdict = judge.run_testcases(problem_id=problem_id, language=language, code=code)
            return Response(verdict, status=201)
        print(request.data)
        return Response(serializer.errors, status=400)
    
class RunCodeAPIView(APIView):
    # authentication_classes = [JWTAuthentication]  # Use JWT authentication
    # permission_classes = [IsAuthenticated]
    serializer_class = RunCodeSerializer
    def post(self, request):
        # breakpoint()
        # code = request.data["code"]
        # language = request.data["language"]
        # input_data = request.data.get("input_data", "")
        serializer = RunCodeSerializer(data=request.data)
        if serializer.is_valid():
            # serializer.save()
            language = serializer.data["language"]
            code = serializer.data["code"]
            input_data = serializer.data.get("input_data", "")
            print(language, code, input_data)
            output = compiler.run_code(language=language, code=code, input_data=input_data)
            return Response(output, status=201)
        return Response(serializer.errors, status=400)
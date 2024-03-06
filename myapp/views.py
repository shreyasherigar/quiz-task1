from django.shortcuts import render
from .models import questions,register,UserResponse
from random import sample
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import questionSerializer,RanquestionSerializer,registerSerializer
from rest_framework import status
from django.contrib.auth.hashers import check_password




# Create your views here.

class RegisterView(APIView):
    def post(self, request):
        try:
            serializer = registerSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"status":"Registered sucessfully","data":serializer.data}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": "username already exists"}, status=status.HTTP_409_CONFLICT)
        
        
class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        print(username)
        print(password)
        if not username or not password:
            return Response({"error": "Username and password are required."}, status=400)
        try:
            user =register.objects.get(username=username)
            if user:
                if check_password(password, user.password):
                    return Response({"message": "Login successful","user_id":user.id}, status=200)
                else:
                    return Response({"error": "Invalid password /password"}, status=401)
            else:
                return Response({"error": "Invalid username"}, status=401)
        except register.DoesNotExist:
                return Response({"error": "Invalid username/password"}, status=401)
        
    

class AddQuestions(APIView):
    def post(self,request):
        question_data=request.data.get('question')
        answer_data=request.data.get('answer')
        if not question_data or not answer_data:
            return Response({"error": "Both are required."}, status=status.HTTP_400_BAD_REQUEST)
        question_instance=questions.objects.create(question=question_data, answer=answer_data)
        
        serializer = questionSerializer(question_instance)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class RandomQuestion(APIView):
    def get(self, request):
        questions_set=questions.objects.all()
        questions_count=questions_set.count()
        
        if questions_count>=5:
            random_questions = sample(list(questions_set), 1)
            serializer = RanquestionSerializer(random_questions, many=True)
            return Response({"status":"Successs","data":serializer.data},status=status.HTTP_200_OK)
        else:
            return Response({"message": "Empty/need more questions"}, status=400)
        
        
class AnswerAPI(APIView):
    def post(self, request):
        question_id = request.data.get('question_id')
        user_answer = request.data.get('answer')
        user_id = request.data.get('user_id')  
        try:
            question = questions.objects.get(id=question_id)
            correct_answer = question.answer
            user_response = UserResponse(user_id=user_id, question=question, user_answer=user_answer)    
            user_responses_count = UserResponse.objects.filter(user_id=user_id).count()
            
            if user_responses_count>=5:
                return Response({'error': 'already attempted 5 questions'}, status=400)
            else:
                user_response.save()
                if user_answer.lower() == correct_answer.lower():     
                    return Response({"message": "Correct answer", "attempts": user_responses_count},status=status.HTTP_200_OK)
                else:
                    return Response({"message": "Incorrect answer.", "attempts": user_responses_count},status=status.HTTP_200_OK)      
        except questions.DoesNotExist:
            return Response({"message": "Question not found"}, status=404)
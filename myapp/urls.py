
from django.urls import path
from .views import RandomQuestion,AddQuestions,RegisterView,LoginView,AnswerAPI

urlpatterns = [
    
    path('register/',RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    
    path('addquestion/',AddQuestions.as_view() ),
    path('question/',RandomQuestion.as_view() ),
    path('answer/',AnswerAPI.as_view()),
   
]

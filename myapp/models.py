from django.db import models

# Create your models here.
class questions(models.Model):
    question=models.CharField(max_length=50,unique=True)
    answer=models.CharField(max_length=50)
    

class register(models.Model):
    name=models.CharField(max_length=50)
    username=models.CharField(max_length=50,unique=True)
    password=models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.name
    

class UserResponse(models.Model):
    user_id = models.CharField(max_length=100)  
    question = models.ForeignKey(questions, on_delete=models.CASCADE)
    user_answer = models.CharField(max_length=255)

    def __str__(self):
        return self.user_id
    

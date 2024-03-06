from rest_framework import serializers
from .models import questions,register
from django.contrib.auth.hashers import make_password

class registerSerializer(serializers.ModelSerializer):
    name=serializers.CharField(required=True)
    username=serializers.CharField(required=True)
    password=serializers.CharField(required=True)
    
    
    def validate_password(self,value):
        value=make_password(value)
        return value
    
    class Meta:
        model = register
        fields = ['name', 'username', 'password']


class loginSerializer(serializers.ModelSerializer):
     class Meta:
        model = register
        fields = ['username', 'password']

class questionSerializer(serializers.ModelSerializer):
    question=serializers.CharField(required=True)
    answer=serializers.CharField(required=True)
    
    class Meta:
        model=questions
        fields = '__all__'
        
class RanquestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = questions
        fields = ['id','question','answer']
        

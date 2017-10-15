from rest_framework import serializers, permissions
from health.models import Notice, Patient, Disease, Ques,Book
from django.contrib.auth.models import User
from rest_framework.decorators import permission_classes

class NoticeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Notice
        fields = ('url', 'subject', 'message', 'attachment1',  'uploaded_at')

class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        fields = ('url', 'p_name', 'p_age', 'p_addr',  'phone_number', 'p_img', 'p_email', 'disease')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email')

class DiseaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Disease
        fields = ('name')

class QuesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ques
        fields = ('url', 'question', 'answer', 'user', 'notice')
        
class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ('url', 'date', 'time','description')
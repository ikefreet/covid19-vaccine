from django import forms
from pybo.models import Reservation, Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question  # 사용할 모델
        fields = ['subject', 'content']  # QuestionForm에서 사용할 Question 모델의 속성

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['NAME', 'BIRTH', 'HOSPITAL', 'VACCINE', 'DATE', 'HOUR']
        labels = {
            'NAME' : '이름',
            'BIRTH' : '생년월일',
            'HOSPITAL' : '병원',
            'VACCINE' : '백신',
            'DATE' : '날짜',
            'HOUR': '시간'
        }
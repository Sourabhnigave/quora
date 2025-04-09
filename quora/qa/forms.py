from django import forms
from .models import Question, Answer, Comment

# Question form
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ask your question...'}),
        }

# Answer form
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['answer_text']
        widgets = {
            'answer_text': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Write your answer...'}),
        }

# Comment form
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']
        widgets = {
            'comment_text': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Write a comment...'}),
        }

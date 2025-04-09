from django.urls import path
from . import views

urlpatterns = [
    path('', views.question_list, name='question_list'),
    path('ask/', views.create_question, name='create_question'),
    path('answer/<int:question_id>/', views.answer_question, name='answer_question'),
    path('like/<int:answer_id>/', views.like_answer, name='like_answer'),
    path('dislike/<int:answer_id>/', views.dislike_answer, name='dislike_answer'),
    path('comment/<int:answer_id>/', views.comment_on_answer, name='comment_on_answer'),
]

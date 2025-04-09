from django.shortcuts import render, redirect, get_object_or_404
from .models import Question, Answer, Upvote, Downvote, Comment
from .forms import QuestionForm, AnswerForm, CommentForm
from django.contrib.auth.decorators import login_required

 


def question_list(request):
    print("User:", request.user)  
    print("Inside create_question") 
    questions = Question.objects.all().order_by('-created_at')
    return render(request, 'qa/question_list.html', {'questions': questions})

def create_question(request):
    print("Inside create_question") 
    print("Is Authenticated:", request.user.is_authenticated)
    if not request.user.is_authenticated:
        print("User is not logged in!")
    else:
        print(f"Authenticated user: {request.user.username}")
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        print(form)
        if form.is_valid():
            question = form.save(commit=False)
            question.created_by = request.user
            question.save()
            return redirect('question_list')
    else:
        form = QuestionForm()
    return render(request, 'qa/create_question.html', {'form': form})

@login_required
def answer_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.user = request.user
            answer.save()
            return redirect('question_list')
    else:
        form = AnswerForm()
    return render(request, 'qa/answer_question.html', {'question': question, 'form': form})

@login_required
def like_answer(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    upvote, created = Upvote.objects.get_or_create(user=request.user, answer=answer)
    if not created:
        upvote.delete()
    return redirect('question_list')


def dislike_answer(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    downvote, created = Downvote.objects.get_or_create(user=request.user, answer=answer)
    if not created:
        downvote.delete()
    return redirect('question_list')

def comment_on_answer(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.answer = answer
            comment.user = request.user
            comment.save()
            return redirect('question_list')
    else:
        form = CommentForm()
    return render(request, 'qa/comment_on_answer.html', {'answer': answer, 'form': form})

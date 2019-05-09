from django.shortcuts import render, get_object_or_404, redirect

from .models import Board, Comment

from django.utils import timezone

from .forms import CommentForm

from .forms2 import CommentForm2

# Create your views here.

def home(request):
    boards = Board.objects
    return render(request, 'home.html', {'boards': boards})

def detail(request, board_id):
    board_detail = get_object_or_404(Board, pk=board_id)
    return render(request, 'detail.html', {'board': board_detail})

def new(request):
    return render(request, 'new.html')

def create(request):
    board = Board()
    board.title = request.GET['title']
    board.body = request.GET['body']
    board.pub_date = timezone.datetime.now()
    board.save()
    return redirect('/myapp/' + str(board.id))

def delete(request, board_id):
    board = Board.objects.get(pk = board_id)
    board.delete()
    return redirect('/')

def edit(request, board_id):
    board_edit = Board.objects.get(pk= board_id)
    return render(request, 'edit.html', {'board': board_edit})

def update(request, board_id):
    board = Board.objects.get(pk= board_id)
    board.title = request.POST['title']
    board.body = request.POST['body']
    board.pub_date = timezone.datetime.now()
    board.save()
    return redirect('/')

def comment_new(request, board_id):
    post = get_object_or_404(Board, pk=board_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = Board.objects.get(pk=board_id)
            comment.save()
            return redirect('detail', board_id)
    else:
        form= CommentForm()
    return render(request, 'board_form.html', {'form':form})

def comment_new2(request, board_id):
    post = get_object_or_404(Board, pk=board_id)
    if request.method == "POST":
        forms = CommentForm2(request.POST)
        if forms.is_valid():
            comment2 = forms.save(commit=False)
            comment2.post = Board.objects.get(pk=board_id)
            comment2.save()
            return redirect('detail', board_id)
    else:
        forms= CommentForm2()
    return render(request, 'board_form2.html', {'forms':forms})

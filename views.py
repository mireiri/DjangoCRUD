from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from diary.forms import NoteForm


# 一覧画面を持ち出す関数
def index(request):
    all_data = Note.objects.all()
    context = {
        'title': '一覧画面',
        'all_data': all_data,
    }
    return render(request, 'diary/index.html', context)

# 新規作成画面を持ち出す関数
def new(request):
    noteform = NoteForm()
    context = {
        'title' : '新規作成画面',
        'noteform': noteform,
    }
    return render(request, 'diary/new.html', context)

# 新規データを登録する関数
def create(request):
    if request.method == 'POST':
        new_data = NoteForm(request.POST)
        if new_data.is_valid():
            new_data.save()
    return redirect('index')
 
# 詳細画面を持ち出す関数   
def detail(request, note_id):
    data = get_object_or_404(Note, pk=note_id)
    context = {
        'title': '詳細画面',
        'data': data,
    }
    return render(request, 'diary/detail.html', context)

# 編集画面を持ち出す関数
def edit(request, note_id):
    data = get_object_or_404(Note, pk=note_id)
    noteform = NoteForm(instance=data)
    context = {
        'title': '編集画面',
        'data': data,
        'noteform': noteform,
    }
    return render(request, 'diary/edit.html', context)

# 更新データを登録する関数
def update(request, note_id):
    if request.method == 'POST':
        data = get_object_or_404(Note, pk=note_id)
        update_data = NoteForm(request.POST, instance=data)
        if update_data.is_valid():
            update_data.save()
    return redirect('index')

# データを削除する関数
def delete(request, note_id):
    delete_data = get_object_or_404(Note, pk=note_id)
    delete_data.delete()
    return redirect('index')

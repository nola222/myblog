from django.shortcuts import render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from account.models import MyUser
from article.models import ArticleTag
from album.models import AlbumInfo
from .models import Board
from django.urls import reverse

# Create your views here.


def board(request, id, page):
    """留言板

    Args:
        request(object): Request
        id(int): 用户id
        page(int): 分页后的某一页

    Returns:

    """
    album = AlbumInfo.objects.filter(user_id=id)
    tag = ArticleTag.objects.filter(user_id=id)
    user = MyUser.objects.filter(id=id).first()
    if not user:
        return redirect(reverse('register'))
    if request.method == 'GET':
        board_list = Board.objects.filter(user_id=id).order_by('-created')
        paginator = Paginator(board_list, 10)
        try:
            page_info = paginator.page(page)
        except PageNotAnInteger:
            page_info = paginator.page(1)
        except EmptyPage:
            page_info = paginator.page(paginator.num_pages)
        return render(request, 'board.html', locals())
    else:
        name = request.POST.get('name')
        email = request.POST.get('email')
        content = request.POST.get('content')
        value = {
            'name': name,
            'email': email,
            'content': content,
            'user_id': id
        }
        Board.objects.create(**value)
        kwargs = {'id': id, 'page': 1}
        return redirect(reverse('board', kwargs=kwargs))

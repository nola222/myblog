from django.shortcuts import render, redirect
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage
from django.urls import reverse
from account.models import MyUser
from album.models import AlbumInfo
from article.models import ArticleTag, ArticleInfo

# Create your views here.


def article(request, id, page):
    """文章信息

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
    ats = ArticleInfo.objects.filter(author_id=id).order_by('-created')
    paginator = Paginator(ats, 10)
    try:
        page_info = paginator.page(page)
    except PageNotAnInteger:
        page_info = paginator.page(1)
    except EmptyPage:
        page_info = paginator.page(paginator.num_pages)
    return render(request, 'article.html', locals())

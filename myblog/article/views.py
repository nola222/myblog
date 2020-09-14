from django.db.models import F
from django.shortcuts import render, redirect
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage
from django.urls import reverse
from account.models import MyUser
from album.models import AlbumInfo
from article.models import ArticleTag, ArticleInfo, Comment

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


def detail(request, id, aId):
    """文章详情

    Args:
        request(Request):
        id(int): 用户id
        aId(int): 文章信息id

    Returns:

    """
    album = AlbumInfo.objects.filter(user_id=id)
    tag = ArticleTag.objects.filter(user_id=id)
    user = MyUser.objects.filter(id=id).first()
    if request.method == 'GET':
        ats = ArticleInfo.objects.filter(id=aId).first()
        atags = ArticleInfo.objects.filter(id=aId).first().article_tag.all()
        cms = Comment.objects.filter(article_id=aId).order_by('-created')
        # 添加阅读量
        if not request.session.get('reading' + str(id) + str(aId), ''):
            reading = ArticleInfo.objects.filter(id=aId)
            reading.update(reading=F('reading') + 1)  # 使用F直接引用字段的值，而不用加载到内存
            request.session['reading' + str(id) + str(aId)] = True
        return render(request, 'detail.html', locals())
    else:
        commentator = request.POST.get('name')
        email = request.POST.get('email')
        content = request.POST.get('content')
        value = {
            'commentator': commentator,
            'email': email,
            'content': content,
            'article_id': aId
        }
        Comment.objects.create(**value)
        kwargs = {'aId': aId, id: 'id'}
        return redirect(reverse('detail', kwargs=kwargs))




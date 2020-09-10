from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import AlbumInfo

# Create your views here.


def album(request, id, page):
    """图片墙

    Args:
        request(object): Request
        id(int): 用户id
        page(int): 图片分页后某一页的页数

    Returns:

    """
    album_list = AlbumInfo.objects.filter(user_id=id).order_by('id')
    paginator = Paginator(album_list, 8)  # per_page=8
    try:
        page_info = paginator.page(page)
    except PageNotAnInteger:  # 若参数page不是整型返回第一页的数据
        page_info = paginator.page(1)
    except EmptyPage:  # 若用户访问的页数比实际页数多，返回最后一页的数据
        page_info = paginator.page(paginator.num_pages)

    return render(request, 'album.html', locals())

